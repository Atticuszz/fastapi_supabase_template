from typing import ClassVar

from app.schemas.base import CreateBase, InDBBase, ResponseBase, UpdateBase


# request
# Properties to receive on item creation
# in
class ItemCreate(CreateBase):
    test_data: str


# Properties to receive on item update
# in
class ItemUpdate(UpdateBase):
    test_data: str


# Properties to return to client
# curd model
# out
class Item(ResponseBase):
    test_data: str

    table_name: ClassVar[str] = "test_table"


# Properties properties stored in DB
class ItemInDB(InDBBase):
    test_data: str
