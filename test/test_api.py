from fastapi.testclient import TestClient
import pytest
from src.api import app

def test_read_example():
    client = TestClient(app)
    response = client.get("/example")
    assert response.status_code == 200
    assert response.json() == {"message": "This is an example endpoint"}
