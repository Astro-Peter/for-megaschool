import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "A test item", "price": 10.0})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Test Item", "description": "A test item", "price": 10.0}}