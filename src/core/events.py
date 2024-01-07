# coding=utf-8
"""
life span events
"""
import logging
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from supabase_py_async import create_client
from supabase_py_async.lib.client_options import ClientOptions
from .supabase_client import supabase_client



@asynccontextmanager
async def lifespan(app: FastAPI):
    """ life span events"""
    identify_worker = None
    try:
        # start client
        await supabase_client.init_supabse()

        yield
    finally:
        logging.info("lifespan shutdown")

