"""
Unit tests for the FastAPI application.
"""
import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.json()
    assert response.json()["Hello"] == "World"


def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "service" in data
    assert data["service"] == "python-project-api"


def test_get_metric_gravity():
    """Test getting gravity in metric units."""
    response = client.get("/gravity/metric")
    assert response.status_code == 200
    
    data = response.json()
    assert "gravity" in data
    assert data["gravity"] == 9.81
    assert data["unit"] == "m/s²"


def test_get_imperial_gravity():
    """Test getting gravity in imperial units."""
    response = client.get("/gravity/imperial")
    assert response.status_code == 200
    
    data = response.json()
    assert "gravity" in data
    assert data["gravity"] == 32.2
    assert data["unit"] == "ft/s²"


def test_post_message():
    """Test posting a message."""
    message_data = {"text": "Hello, API!"}
    response = client.post("/message", json=message_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "received_message" in data
    assert data["received_message"] == "Hello, API!"
    assert "echo_back" in data
    assert data["echo_back"] == "Echo: Hello, API!"
    assert "timestamp" in data


def test_read_item_path_only():
    """Test reading an item with just path parameter."""
    item_id = 42
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["item_id"] == item_id
    assert "description" in data
    assert str(item_id) in data["description"]


def test_read_item_with_query():
    """Test reading an item with both path and query parameters."""
    item_id = 42
    query_param = "test_query"
    response = client.get(f"/items/{item_id}?q={query_param}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["item_id"] == item_id
    assert "query" in data
    assert data["query"] == query_param
    assert "description" in data
    assert query_param in data["description"]