"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 05/01/2024
@Description  :
"""
import logging
import os
from typing import List, Union

from pydantic import AnyHttpUrl, validator, Field

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

log_format = logging.Formatter('%(asctime)s : %(levelname)s - %(message)s')

# root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# standard stream handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_format)
root_logger.addHandler(stream_handler)

logger = logging.getLogger(__name__)
load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SUPABASE_URL: str = Field(default_factory=lambda: os.getenv("SUPABASE_URL"))
    SUPABASE_KEY: str = Field(default_factory=lambda: os.getenv("SUPABASE_KEY"))

    # SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl = "localhost"
    SERVER_PORT：int = 8000
    # # TODO: the following  need to follow the newest version of fastapi
    # # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    #
    # @validator("BACKEND_CORS_ORIGINS", pre=True)
    # def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)
    #
    PROJECT_NAME: str = "fastapi supabase template"

    class Config:
        """sensitive to lowercase"""
        case_sensitive = True


settings = Settings()
