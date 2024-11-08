import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

from app.models import Item


class User(SQLModel, table=True):
    # __table_args__ = {'extend_existing': True, 'autoload': True}
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(max_length=255)
    items: list["Item"] = Relationship(back_populates="owner", cascade_delete=True)
