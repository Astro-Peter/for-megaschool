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
import pytest
from fastapi.testclient import TestClient
from src.api.app import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    # Set up database connection here if needed
    yield
    # Teardown database connection here if needed


def test_create_item(test_db):
    response = client.post("/items/", json={"name": "Test Item", "description": "A test item", "price": 10.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"


def test_read_item(test_db):
    response = client.get("/items/1")  # Assuming the ID of the item created above is 1
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"