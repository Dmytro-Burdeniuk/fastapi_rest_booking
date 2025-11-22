from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.auth.jwt import get_password_hash, verify_password
from src.database.models import User
from src.schemas import UserCreate


def create_user(db: Session, user_in: UserCreate) -> User:
    stmt = select(User).where(User.email == user_in.email)
    existing = db.execute(stmt).scalar_one_or_none()
    if existing:
        raise ValueError("User with this email already exists.")

    user = User(
        email=user_in.email,
        name=user_in.name,
        password_hash=get_password_hash(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    stmt = select(User).where(User.email == email)
    user = db.execute(stmt).scalar_one_or_none()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user
