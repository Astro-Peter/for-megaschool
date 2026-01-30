import pytest
from fastapi.testclient import TestClient
from src.main import app

test_client = TestClient(app)

def test_read_root():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}


def test_create_item():
    response = test_client.post("/items/", json={"name": "Item 1"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Item 1"}}


def test_update_item():
    response = test_client.put("/items/1", json={"name": "Updated Item 1"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "item": {"name": "Updated Item 1"}}


def test_delete_item():
    response = test_client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted", "item_id": 1}