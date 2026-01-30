import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_create_item():
    response = client.post("/items/", json={"name": "Item1", "description": "A sample item", "price": 10.5, "tax": 2.0})
    assert response.status_code == 200
    assert response.json() == {"name": "Item1", "description": "A sample item", "price": 10.5, "tax": 2.0}