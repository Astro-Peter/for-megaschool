from fastapi.testclient import TestClient
from src.main import app

def test_read_item():
    client = TestClient(app)
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "name": "Item Name"}
