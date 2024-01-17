import pytest
from lambda_function import *
import json

def test_lambda_handler():
    event = {
        "test": "test"
    }
    context = {
        "test": "test"
    }
    response = lambda_handler(event, context)
    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == event
