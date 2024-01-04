import json

import pytest
from lib.exceptions import APIException


@pytest.mark.parametrize(
    "resp",
    [
        # happy path
        {"status_code": 200, "content": "Hello world 0.1.0"}
    ],
)
def test_hello(
    resp: dict, test_client
):

    response = test_client.get(url="/hello")
    if isinstance(response, APIException):
        assert response.status_code == resp.status_code
        assert json.loads(response.text) == resp.content()
    else:
        assert response.status_code == resp.get("status_code")
        assert json.loads(response.content) == resp.get("content")
