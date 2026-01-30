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


def test_create_item():
    response = client.post("/items/", json={"name": "item name"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "item name"}}



def test_create_item():
    response = client.post("/items/", json={"name": "item name"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "item name"}}
