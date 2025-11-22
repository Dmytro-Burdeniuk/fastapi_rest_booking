from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import Event, User
from src.schemas import EventCreate


def get_all_events(db: Session) -> list[Event]:
    stmt = select(Event)
    result = db.execute(stmt)
    return list(result.scalars().all())


def create_event(db: Session, event_in: EventCreate, user: User) -> Event:
    event = Event(
        title=event_in.title,
        description=event_in.description,
        datetime=event_in.datetime,
        max_seats=event_in.max_seats,
        owner_id=user.id,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def get_my_events(db: Session, user: User) -> list[Event]:
    stmt = select(Event).where(Event.owner_id == user.id)
    result = db.execute(stmt)
    return list(result.scalars().all())
