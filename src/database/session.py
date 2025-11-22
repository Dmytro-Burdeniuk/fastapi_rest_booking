from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

from src.config import settings


class Base(DeclarativeBase):
    pass


class DBSessionManager:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url)
        self._session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        db: Session = self._session_factory()
        try:
            yield db
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()


db_session_manager = DBSessionManager(settings.database_url)


def get_db() -> Generator[Session, None, None]:
    with db_session_manager.session() as db:
        yield db
