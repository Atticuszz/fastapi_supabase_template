from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src import crud
from src.api.deps import SessionDep
from src.schemas.auth import UserOut, UserCreate, UserUpdate
from src.schemas.msg import Massage

router = APIRouter()


@router.post("/login/access-token", response_model=UserOut)
async def login_access_token(
        session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> UserOut:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = await crud.user.authenticate(session, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return user


@router.post(
    "/", response_model=UserOut
)
async def create_user_by_email(*, session: SessionDep, user_in: UserCreate) -> UserOut:
    """
    Create new user.
    """
    user = await crud.user.create_user_by_email(session=session, user_create=user_in)
    # NOTE: no need to verify email here
    # TODO: what exception will raise if user already existed?
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return user


@router.put("/update_user")
def update_user(
        *,
        session: SessionDep,
        user_in: UserUpdate,
) -> Massage:
    """
    Update a user.
    """
    user = crud.user.update(session=session, user_update=user_in)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return Massage(Msg="User updated")

# @router.post("/login/test-token", response_model=UserOut)
# def test_token(current_user: CurrentUser) -> Any:
#     """
#     Test access token
#     """
#     return current_user
