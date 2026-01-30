import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)
from src.main import testFunction


class TestSum(unittest.TestCase):
    def test_testFunction(self):
        """
        Test that it can sum a list of integers
        """
        self.assertTrue(testFunction())


if __name__ == '__main__':
    unittest.main()


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_item():
    response = client.post("/items/", json={"name": "item1"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "item1"}}


def test_update_item():
    response = client.put("/items/1", json={"name": "updated_item"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "item": {"name": "updated_item"}}