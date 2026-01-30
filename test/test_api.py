import pytest
from fastapi.testclient import TestClient
from src.api import app

test_client = TestClient(app)

def test_read_root():
    response = test_client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_create_item():
    response = test_client.post("/items/", json={"name": "Item1", "description": "A new item", "price": 12.99})
    assert response.status_code == 200
    assert response.json() == {"name": "Item1", "description": "A new item", "price": 12.99}