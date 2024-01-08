from typing import Optional

from gotrue import User
from pydantic import BaseModel, EmailStr


# Shared properties


## request
# Properties to receive via API on creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(BaseModel):
    password: Optional[str] = None


## response
class UserOut(User):
    access_token: str


## db
class UserInDBBase(User):
    pass


# Additional properties to return via API
class User(UserInDBBase):
    pass

# Additional properties stored in DB
