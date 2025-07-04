from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel, Field

Base = declarative_base()

# PUBLIC_INTERFACE
class Note(Base):
    """
    SQLAlchemy ORM model for a Note.
    """
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# PUBLIC_INTERFACE
class NoteCreate(BaseModel):
    """
    Pydantic schema for creating a Note.
    """
    title: str = Field(..., description="Title of the note", max_length=200)
    content: Optional[str] = Field(None, description="Content of the note")


# PUBLIC_INTERFACE
class NoteResponse(BaseModel):
    """
    Pydantic schema for returning Note data in API responses.
    """
    id: int = Field(..., description="Unique ID of the note")
    title: str = Field(..., description="Title of the note")
    content: Optional[str] = Field(None, description="Content of the note")
    created_at: datetime = Field(..., description="Timestamp when the note was created")
    updated_at: datetime = Field(..., description="Timestamp when the note was last updated")

    class Config:
        orm_mode = True
