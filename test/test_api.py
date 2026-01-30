import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_item():
    response = client.post("/items/", json={"name": "Item1", "price": 10.5})
    assert response.status_code == 200
    assert response.json() == {"name": "Item1", "price": 10.5, "is_available": true}



def test_create_item():
    response = client.post('/items/', json={'name': 'Item1', 'price': 10.5})
    assert response.status_code == 200
    assert response.json() == {'name': 'Item1', 'price': 10.5, 'is_available': True}
