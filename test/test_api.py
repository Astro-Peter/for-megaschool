import pytest
from fastapi.testclient import TestClient
from src.main import app

test_client = TestClient(app)

def test_read_root():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}


def test_read_item():
    response = test_client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}
