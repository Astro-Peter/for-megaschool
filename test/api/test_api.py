import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5}

def test_create_item():
    response = client.post("/items/", json={"name": "Item 1", "price": 10.0})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Item 1", "price": 10.0}}