"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 05/01/2024
@Description  :
"""
import logging

from gotrue import User
from supabase_py_async import create_client, AsyncClient
from supabase_py_async.lib.client_options import ClientOptions

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from ..core.config import settings
from ..core.events import super_client

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)
TokenDep = Annotated[str, Depends(reusable_oauth2)]


async def validate_user(token: str = Depends(reusable_oauth2)) -> str:
    prefix = "Bearer "
    if not token.startswith(prefix):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = token[len(prefix):]
    try:
        await super_client.auth.get_user(access_token)
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=401, detail=e)
    return access_token


AccessTokenDep = Annotated[str, Depends(validate_user)]


async def get_db(access_token: AccessTokenDep) -> AsyncClient:
    client: AsyncClient | None = None
    try:
        client = await create_client(settings.SUPABASE_URL, access_token, options=ClientOptions(
            postgrest_client_timeout=10, storage_client_timeout=10))
        yield client
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=401, detail=e)
    finally:
        if client:
            await client.auth.sign_out()


SessionDep = Annotated[AsyncClient, Depends(get_db)]


async def get_current_user(session: SessionDep) -> User:
    user = await session.auth.get_user()
    if not user:
        logging.error("User not found")
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
