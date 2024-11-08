import logging

import pytest
from sqlmodel import Session

from src.app.api.deps import engine
from src.app.core.db import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.anyio
async def test_init_db() -> None:
    with Session(engine) as session:
        await init_db(session)
