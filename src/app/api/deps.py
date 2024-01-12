"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 05/01/2024
@Description  :
"""
import logging
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from gotrue import User
from supabase_py_async import AsyncClient, create_client
from supabase_py_async.lib.client_options import ClientOptions

from app.core.config import settings


async def supser_client() -> AsyncClient:
    client: AsyncClient | None = None
    try:
        client = await create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY,
            options=ClientOptions(
                postgrest_client_timeout=10, storage_client_timeout=10
            ),
        )
        yield client
    finally:
        if client:
            await client.auth.sign_out()


SuperClientDep = Annotated[AsyncClient, Depends(supser_client)]

# auto get access_token from header
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="please login by supabase-js to get token"
)

TokenDep = Annotated[str, Depends(reusable_oauth2)]


async def validate_user(access_token: TokenDep, super_client: SuperClientDep) -> str:
    try:
        if not super_client:
            raise HTTPException(status_code=401, detail="No super client")
        await super_client.auth.get_user(access_token)
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=401, detail=e)
    return access_token


AccessTokenDep = Annotated[str, Depends(validate_user)]


async def get_db(access_token: AccessTokenDep) -> AsyncClient:
    client: AsyncClient | None = None
    try:
        client = await create_client(
            settings.SUPABASE_URL,
            access_token,
            options=ClientOptions(
                postgrest_client_timeout=10, storage_client_timeout=10
            ),
        )
        # client.postgrest.auth(token=access_token)
        # await client.auth.get_user(access_token)
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
