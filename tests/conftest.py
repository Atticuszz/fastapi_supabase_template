import logging
import os
from collections.abc import AsyncGenerator, Generator
from logging.handlers import RotatingFileHandler
from pathlib import Path

import pytest
from _pytest.config import Config
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from supabase_py_async import AsyncClient, create_client

from app.main import app

LOG_FILE = Path(__file__).parent / "scripts.log"


# 日志配置函数
def setup_logging(level: int = logging.INFO) -> None:
    # 创建 Logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # 创建用于写入日志文件的 Handler
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=1024 * 1024 * 5, backupCount=5
    )
    file_handler.setLevel(level)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    # 创建用于控制台输出的 Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # 添加 Handlers 到 Logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


setup_logging()


def pytest_configure(config: Config) -> None:
    load_dotenv(dotenv_path="tests/tests.env")


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c



@pytest.fixture(scope="module")
async def db() -> AsyncGenerator[AsyncClient, None]:
    url = os.environ.get("SUPABASE_TEST_URL")
    assert url is not None, "Must provide SUPABASE_TEST_URL environment variable"
    key = os.environ.get("SUPABASE_TEST_KEY")
    assert key is not None, "Must provide SUPABASE_TEST_KEY environment variable"
    db_client = await create_client(url, key)
    await db_client.auth.sign_in_with_password(
        {"email": "zhouge1831@gmail.com", "password": "Zz030327#"}
    )
    get_session = await db_client.auth.get_session()
    assert get_session.user is not None
    logging.info("db_client.get_session", get_session.user.model_dump())
    try:
        yield db_client  # 提供数据库客户端给测试用例
    finally:
        if db_client:
            await db_client.auth.sign_out()
