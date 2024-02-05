"""
life span events
"""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.deps import init_super_client


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """life span events"""
    try:
        await init_super_client()
        yield
    finally:
        logging.info("lifespan shutdown")
