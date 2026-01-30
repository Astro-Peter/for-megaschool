from fastapi.testclient import TestClient
from main import app

def test_read_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    client = TestClient(app)
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "query_param": None}
    
    response = client.get("/items/5?query_param=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "query_param": "test"}
