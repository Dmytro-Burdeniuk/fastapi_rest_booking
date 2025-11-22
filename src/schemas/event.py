from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    datetime: datetime
    max_seats: int = Field(..., gt=0)


class EventCreate(EventBase):
    pass


class EventOut(EventBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True