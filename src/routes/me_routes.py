from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.jwt import get_current_user
from src.database.session import get_db
from src.database.models import User
from src.repo.event_repo import get_my_events
from src.repo.booking_repo import get_my_bookings
from src.schemas import EventOut, BookingWithEventOut

router = APIRouter(prefix="/my", tags=["me"])


@router.get("/events", response_model=List[EventOut])
def my_events(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_my_events(db, current_user)


@router.get("/bookings", response_model=List[BookingWithEventOut])
def my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    bookings = get_my_bookings(db, current_user)
    return bookings