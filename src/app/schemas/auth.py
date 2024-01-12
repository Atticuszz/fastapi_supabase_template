from gotrue import User, UserAttributes
from pydantic import BaseModel


# Shared properties
class Token(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None
    expires_at: int | None = None
    """
    A timestamp of when the token will expire. Returned when a login is confirmed.
    """
    token_type: str


# request
# Properties to receive via API on creation
# in
class UserCreate(BaseModel):
    pass


# Properties to receive via API on update
# in
class UserUpdate(UserAttributes):
    pass


# response


class UserInDBBase(BaseModel):
    pass


# Properties to return to client via api
# out
class UserOut(Token):
    pass


# Properties properties stored in DB
class UserInDB(User):
    pass
