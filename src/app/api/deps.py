import logging
from collections.abc import Generator
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, create_engine

from app.core.config import settings
from app.schemas.auth import UserIn
from supabase._async.client import AsyncClient, create_client
from supabase.lib.client_options import ClientOptions


async def get_super_client() -> AsyncClient:
    """for validation access_token init at life span event"""
    super_client = await create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_KEY,
        options=ClientOptions(postgrest_client_timeout=10, storage_client_timeout=10),
    )
    if not super_client:
        raise HTTPException(status_code=500, detail="Super client not initialized")
    return super_client


SuperClient = Annotated[AsyncClient, Depends(get_super_client)]

# auto get access_token from header
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="Token")
AccessTokenDep = Annotated[str, Depends(reusable_oauth2)]


async def get_current_user(
    access_token: AccessTokenDep, super_client: SuperClient
) -> UserIn:
    """get current user from access_token and  validate same time"""
    user_rsp = await super_client.auth.get_user(jwt=access_token)
    if not user_rsp:
        logging.error("User not found")
        raise HTTPException(status_code=404, detail="User not found")
    return UserIn(**user_rsp.user.model_dump(), access_token=access_token)


CurrentUser = Annotated[UserIn, Depends(get_current_user)]


engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
