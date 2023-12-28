import json

import pytest
from main import app
from starlette.testclient import TestClient

@pytest.fixture(scope="session")
def test_client():
    client = TestClient(app)
    with open("openapi_spec.json", "w", encoding="utf-8") as f:
        json.dump(app.openapi(), f, ensure_ascii=False, indent=2)
    yield client

