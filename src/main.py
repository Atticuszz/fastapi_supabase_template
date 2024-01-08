"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 05/01/2024
@Description  :
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.api_v1.api import api_router
from src.core import lifespan
from src.core.config import settings


def create_app() -> FastAPI:
    # init FastAPI with lifespan
    app = FastAPI(lifespan=lifespan)
    # set CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include the routers
    app.include_router(api_router, prefix=settings.API_V1_STR)

    return app


app = create_app()

if __name__=="__main__":
    host = 'localhost'
    port = 5000
    uvicorn.run(app, host=host, port=port)

