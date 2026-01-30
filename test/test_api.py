import sys
import os
import pytest
from fastapi.testclient import TestClient
from datetime import datetime
import json

# Add src directory to path to properly import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.api.main import app

# Create a test client for the API
client = TestClient(app)

def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "FastAPI API Service"
    assert data["status"] == "running"


def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert isinstance(data["timestamp"], int)


def test_create_and_read_item():
    """Test creating and reading an item"""
    # Create an item
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99,
        "tax": 1.50
    }
    
    response = client.post("/items/", json=item_data)
    assert response.status_code == 201
    
    created_item = response.json()
    assert created_item["name"] == "Test Item"
    assert created_item["description"] == "A test item"
    assert created_item["price"] == 10.99
    assert created_item["tax"] == 1.50
    assert "id" in created_item
    assert "created_at" in created_item
    
    # Get the created item by ID
    item_id = created_item["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    
    retrieved_item = response.json()
    assert retrieved_item["id"] == item_id
    assert retrieved_item["name"] == "Test Item"


def test_list_items():
    """Test listing items"""
    # First create multiple items
    item_data1 = {
        "name": "First Item",
        "description": "First test item",
        "price": 15.99,
        "tax": 2.00
    }
    
    item_data2 = {
        "name": "Second Item", 
        "description": "Second test item",
        "price": 20.50,
        "tax": 3.50
    }
    
    client.post("/items/", json=item_data1)
    client.post("/items/", json=item_data2)
    
    # Get the list of all items
    response = client.get("/items/")
    assert response.status_code == 200
    
    items = response.json()
    assert isinstance(items, list)
    assert len(items) >= 2  # Might include previously created items
    
    # Check that both items are in the response
    names = [item["name"] for item in items]
    assert "First Item" in names
    assert "Second Item" in names


def test_update_item():
    """Test updating an existing item"""
    # Create an item first
    item_data = {
        "name": "Original Item",
        "description": "Original description",
        "price": 10.00,
        "tax": 1.00
    }
    
    response = client.post("/items/", json=item_data)
    assert response.status_code == 201
    
    item_id = response.json()["id"]
    
    # Update the item
    updated_data = {
        "name": "Updated Item",
        "description": "Updated description",
        "price": 15.00,
        "tax": 1.50
    }
    
    response = client.put(f"/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    
    updated_item = response.json()
    assert updated_item["id"] == item_id
    assert updated_item["name"] == "Updated Item"
    assert updated_item["description"] == "Updated description"
    assert updated_item["price"] == 15.00
    assert updated_item["tax"] == 1.50


def test_delete_item():
    """Test deleting an item"""
    # Create an item first
    item_data = {
        "name": "Item to Delete",
        "description": "This item will be deleted",
        "price": 5.00,
        "tax": 0.50
    }
    
    response = client.post("/items/", json=item_data)
    assert response.status_code == 201
    
    item_id = response.json()["id"]
    
    # Verify it exists
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    
    # Delete the item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    
    # Verify it no longer exists
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404


def test_get_nonexistent_item():
    """Test attempting to get a non-existent item"""
    response = client.get("/items/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_update_nonexistent_item():
    """Test attempting to update a non-existent item"""
    update_data = {"name": "Updated Name"}
    response = client.put("/items/99999", json=update_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}