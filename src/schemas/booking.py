from pydantic import BaseModel, Field

from src.schemas.event import EventOut


class BookingCreate(BaseModel):
    seats: int = Field(..., gt=0)


class BookingOut(BaseModel):
    id: int
    user_id: int
    event_id: int
    seats_booked: int

    class Config:
        orm_mode = True


class BookingWithEventOut(BaseModel):
    id: int
    seats_booked: int
    event: EventOut 

    class Config:
        orm_mode = True