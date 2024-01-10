from typing import Optional

from gotrue import User, UserAttributes, AuthResponse
from pydantic import BaseModel, EmailStr


# Shared properties

## request
# Properties to receive via API on creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserAttributes):
    pass


## response
class UserOut(User):
    access_token: str | None = None
    expires_at: int | None = None
    """
    A timestamp of when the token will expire. Returned when a login is confirmed.
    """
    token_type: str

    @classmethod
    def from_auth_rsp(cls, auth_rsp: AuthResponse) -> "UserOut":
        return cls(**auth_rsp.user.model_dump(), access_token=auth_rsp.session.access_token,
                   expires_at=auth_rsp.session.expires_at, token_type=auth_rsp.session.token_type)


## db
# user ，simplest name var is db model


# Additional properties to return via API

# Additional properties stored in DB
