"""
Database utilities and session management for FastAPI routes using SQLAlchemy and SQLite.
This sets up the SQLAlchemy engine, session local, declarative base, and dependency injection for FastAPI endpoints.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import Generator

from .models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./notes.db"

# The 'connect_args' is needed only for SQLite.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# PUBLIC_INTERFACE
def get_db() -> Generator[Session, None, None]:
    """
    Dependency generator for FastAPI routes to provide a database session.
    Yields:
        db: SQLAlchemy Session object (closed after request finishes).
    Usage:
        Inject in FastAPI endpoints with: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Expose Base for Alembic or manual use (Base.metadata.create_all).
DeclarativeBase: DeclarativeMeta = Base
