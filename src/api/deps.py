"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 05/01/2024
@Description  :
"""
from fastapi import Header, HTTPException
from gotrue import AuthResponse
from gotrue.errors import AuthSessionMissingError

from ..core.config import logger


async def validate_user(authorization: str | None = Header(None), refresh_token: str | None = Header(None)):
    """
    Validate user session with access and refresh tokens
    :param authorization: Authorization header containing the access token
    :param refresh_token: Header containing the refresh token
    """
    from app.core.supabase_client import supabase_client
    if not authorization or not refresh_token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    tokens = authorization.split(" ")
    if len(tokens) != 2 or tokens[0].lower() != "bearer":
        raise HTTPException(status_code=401,
                            detail="Invalid authorization header format")

    access_token = tokens[1]

    try:
        # Assuming set_session requires both access and refresh tokens
        response: AuthResponse = await supabase_client.set_session(access_token=access_token,
                                                                   refresh_token=refresh_token)
        logger.info(f"User {response.user.email} request validated")
        return response.session
    except AuthSessionMissingError as e:
        raise HTTPException(status_code=401, detail=e.message)
