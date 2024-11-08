from sqlmodel import SQLModel

from .item import Item
from .user import User

__all__ = ["User", "Item", "Message"]


# Generic message
class Message(SQLModel):
    message: str
