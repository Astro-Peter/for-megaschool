import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API"}


def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}


def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) == 0  # Initially, the list should be empty


def test_create_item():
    response = client.post("/items/", json={"name": "item name"})
    assert response.status_code == 200
    assert response.json() == {"item": {"item_id": 1, "name": "item name"}}


def test_create_second_item():
    response = client.post("/items/", json={"name": "second item"})
    assert response.status_code == 200
    assert response.json() == {"item": {"item_id": 2, "name": "second item"}}


def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 deleted"}
    response = client.get("/items/")
    assert len(response.json()) == 1
