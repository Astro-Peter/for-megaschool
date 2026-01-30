import pytest
from fastapi.testclient import TestClient
from src.main_api import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_item():
    item_data = {"name": "item1", "description": "A test item", "price": 10.5, "tax": 0.5}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data


def test_create_item_with_tax():
    item_data = {"name": "item2", "description": "Another test item", "price": 20.5, "tax": 0.5}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data
