import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}

def test_create_item():
    response = client.post("/items/", json={"name": "item1", "price": 10.0})
    assert response.status_code == 200
    assert response.json() == {"message": "Item created", "item": {"name": "item1", "price": 10.0}}