"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 05/01/2024
@Description  :
"""
import logging
from typing import Annotated

from fastapi import Cookie, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from gotrue import User
from gotrue.errors import AuthApiError
from supabase_py_async import AsyncClient, create_client
from supabase_py_async.lib.client_options import ClientOptions

from app.core.config import settings
from app.schemas import Token

# auto get access_token from header
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="please login by supabase-js to get token"
)
AccessTokenDep = Annotated[str, Depends(reusable_oauth2)]
RefreshTokenDep = Annotated[str | None, Cookie()]


async def get_token(
    access_token: AccessTokenDep, refresh_token: RefreshTokenDep
) -> Token | None:
    if not access_token:
        raise HTTPException(status_code=401, detail="No access token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="No refresh token")
    return Token(access_token=access_token, refresh_token=refresh_token)


TokenDep = Annotated[Token | None, Depends(get_token)]


async def get_db(token: TokenDep) -> AsyncClient:
    client: AsyncClient | None = None
    try:
        client = await create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY,
            options=ClientOptions(
                postgrest_client_timeout=10, storage_client_timeout=10
            ),
        )
        # checks all done in supabase-py !
        if not token:
            raise HTTPException(status_code=401, detail="Invalid authentication")
        await client.auth.set_session(token.access_token, token.refresh_token)
        # session = await client.auth.get_session()
        yield client

    except AuthApiError as e:
        logging.error(e)
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )
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
