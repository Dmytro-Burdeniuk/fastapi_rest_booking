from datetime import datetime
from typing import List, Optional

from sqlalchemy import ForeignKey, String, Text, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    events: Mapped[List["Event"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan"
    )
    bookings: Mapped[List["Booking"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    datetime: Mapped[datetime] = mapped_column(DateTime)
    max_seats: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner: Mapped[User] = relationship(back_populates="events")
    bookings: Mapped[List["Booking"]] = relationship(
        back_populates="event", cascade="all, delete-orphan"
    )


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    seats_booked: Mapped[int] = mapped_column(Integer)

    user: Mapped[User] = relationship(back_populates="bookings")
    event: Mapped[Event] = relationship(back_populates="bookings")