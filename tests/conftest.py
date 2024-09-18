import logging
import os
from collections.abc import AsyncGenerator, Generator
from logging.handlers import RotatingFileHandler
from pathlib import Path

import pytest
from dotenv import load_dotenv
from faker import Faker
from fastapi.testclient import TestClient
from pydantic import ConfigDict
from supabase._async.client import AsyncClient, create_client

from app.main import app
from app.schemas import Token
from tests.utils import get_auth_header

LOG_FILE = Path(__file__).parent / "scripts.log"


def setup_logging(level: int = logging.INFO) -> None:
    logger = logging.getLogger()
    logger.setLevel(level)

    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=1024 * 1024 * 5, backupCount=5
    )
    file_handler.setLevel(level)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


setup_logging()


@pytest.fixture(scope="module")
def anyio_backend() -> str:
    return "asyncio"


def pytest_configure(config: ConfigDict) -> None:
    load_dotenv()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
async def token() -> AsyncGenerator[Token, None]:
    url = os.environ.get("SUPABASE_TEST_URL")
    assert url is not None, "Must provide SUPABASE_TEST_URL environment variable"
    key = os.environ.get("SUPABASE_TEST_KEY")
    assert key is not None, "Must provide SUPABASE_TEST_KEY environment variable"
    db_client = await create_client(url, key)
    fake_email = Faker().email()
    fake_password = Faker().password()
    response = await db_client.auth.sign_up(
        {"email": fake_email, "password": fake_password}
    )
    assert response.user.email == fake_email
    assert response.user.id is not None
    assert response.session.access_token is not None

    yield Token(
        access_token=response.session.access_token,
    )


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
    # logging.info("db_client.get_session", get_session.user.model_dump())
    try:
        yield db_client
    finally:
        if db_client:
            await db_client.auth.sign_out()


@pytest.mark.anyio
async def test_read_all_items(client: TestClient, token: Token) -> None:
    headers = get_auth_header(token.access_token)

    response = client.get(
        "/api/v1/items/read-all-item",
        headers=headers,
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
