from typing import Generator

import pytest
from fastapi.testclient import TestClient

from ngr.main import app


@pytest.fixture(scope='session')
def client() -> Generator:
    with TestClient(app) as client:
        yield client
