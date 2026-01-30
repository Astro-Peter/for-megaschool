import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
from src.main import testFunction


class TestSum(unittest.TestCase):
    def test_testFunction(self):
        """
        Test that it can sum a list of integers
        """
        self.assertTrue(testFunction())


if __name__ == '__main__':
    unittest.main()
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item():
    response = client.post("/items", json={"name": "Item 1"})
    assert response.status_code == 200
    assert response.json() == {"name": "Item 1"}

def test_read_item():
    response = client.post("/items", json={"name": "Item 1"})
    item_id = 0
    response = client.get(f"/items/{{item_id}}")
    assert response.status_code == 200
    assert response.json() == {"name": "Item 1"}

def test_update_item():
    response = client.put("/items/0", json={"name": "Updated Item 1"})
    assert response.status_code == 200
    assert response.json() == {"name": "Updated Item 1"}

def test_delete_item():
    response = client.delete("/items/0")
    assert response.status_code == 200
    assert response.json() == {"name": "Updated Item 1"}