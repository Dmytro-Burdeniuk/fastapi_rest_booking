from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.auth.jwt import get_current_user
from src.database.session import get_db
from src.database.models import User
from src.repo.event_repo import get_all_events, create_event
from src.repo.booking_repo import book_event
from src.schemas import EventCreate, EventOut, BookingCreate, BookingOut

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=List[EventOut])
def list_events(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_events(db)


@router.post("", response_model=EventOut, status_code=status.HTTP_201_CREATED)
def create_event_route(
    event_in: EventCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_event(db, event_in, current_user)


@router.post("/{event_id}/book", response_model=BookingOut, status_code=status.HTTP_201_CREATED)
def book_event_route(
    event_id: int,
    booking_in: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        booking = book_event(db, event_id, booking_in, current_user)
    except LookupError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    return booking