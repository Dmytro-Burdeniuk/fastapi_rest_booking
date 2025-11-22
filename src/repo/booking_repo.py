from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload

from src.database.models import Booking, Event, User
from src.schemas import BookingCreate


def book_event(
    db: Session,
    event_id: int,
    booking_in: BookingCreate,
    user: User,
) -> Booking:
    stmt_event = select(Event).where(Event.id == event_id)
    event = db.execute(stmt_event).scalar_one_or_none()
    if not event:
        raise LookupError("Event not found.")

    stmt_existing = select(Booking).where(
        Booking.user_id == user.id,
        Booking.event_id == event_id,
    )
    existing_booking = db.execute(stmt_existing).scalar_one_or_none()
    if existing_booking:
        raise ValueError("You already have a booking for this event.")

    total_booked_stmt = select(func.sum(Booking.seats_booked)).where(
        Booking.event_id == event_id
    )
    total_booked = db.execute(total_booked_stmt).scalar() or 0

    remaining = event.max_seats - total_booked
    if booking_in.seats > remaining:
        raise ValueError(f"Not enough seats. Remaining: {remaining}.")

    booking = Booking(
        user_id=user.id,
        event_id=event.id,
        seats_booked=booking_in.seats,
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


def get_my_bookings(db: Session, user: User) -> list[Booking]:
    stmt = (
        select(Booking)
        .options(joinedload(Booking.event))
        .where(Booking.user_id == user.id)
    )
    result = db.execute(stmt)
    return list(result.scalars().all())
