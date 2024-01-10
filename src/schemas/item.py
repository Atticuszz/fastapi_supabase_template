from pydantic import BaseModel

## request

# Shared properties
class ItemBase(BaseModel):
    # where the data
    table_name: str



# Properties to receive on item creation
# in
class ItemCreate(ItemBase):
    # inherent to add more properties for creating
    pass


# Properties to receive on item update
# in
class ItemUpdate(ItemBase):
    # inherent to add more properties for updating
    id：str

## response

# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: str
    user_id: str
    created_at: str



# Properties to return to client
# out
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
