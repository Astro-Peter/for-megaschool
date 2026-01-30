from fastapi.testclient import TestClient
from src.main_api import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post("/items/", json={"name": "item1", "description": "A test item", "price": 10.5})
    assert response.status_code == 200
    assert response.json() == {"name": "item1", "description": "A test item", "price": 10.5}