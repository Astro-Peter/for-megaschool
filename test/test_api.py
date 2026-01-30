import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "price": 12.5})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Test Item", "price": 12.5}, "message": "Item created!"}