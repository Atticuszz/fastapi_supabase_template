# coding=utf-8
"""
life span events
"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from supabase_py_async import AsyncClient, create_client
from supabase_py_async.lib.client_options import ClientOptions

from src.core.config import settings

super_client: AsyncClient | None = None


async def create_super_client() -> AsyncClient:
    return await create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY, options=ClientOptions(
        postgrest_client_timeout=10, storage_client_timeout=10))


@asynccontextmanager
async def lifespan(app: FastAPI):
    """ life span events"""
    identify_worker = None
    global super_client
    try:
        # start client
        super_client = await create_super_client()

        yield
    finally:
        logging.info("lifespan shutdown")
