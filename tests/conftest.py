import os
from collections.abc import AsyncGenerator, Generator

import pytest
from _pytest.config import Config
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from supabase_py_async import AsyncClient, create_client

from app.main import app


def pytest_configure(config: Config) -> None:
    load_dotenv(dotenv_path="tests/tests.env")


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


# FIXME: AttributeError: 'async_generator' object has no attribute 'table'
@pytest.fixture(scope="module")
@pytest.mark.anyio
async def db() -> AsyncGenerator[AsyncClient, None]:
    url = os.environ.get("SUPABASE_TEST_URL")
    assert url is not None, "Must provide SUPABASE_TEST_URL environment variable"
    key = os.environ.get("SUPABASE_TEST_KEY")
    assert key is not None, "Must provide SUPABASE_TEST_KEY environment variable"
    db_client = await create_client(url, key)
    try:
        yield db_client  # 提供数据库客户端给测试用例
    finally:
        if db_client:
            await db_client.auth.sign_out()
