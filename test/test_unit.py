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
from src.main import app

test_client = TestClient(app)

def test_read_root():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_item():
    response = test_client.post("/items/", json={"name": "test item"})
    assert response.status_code == 200
    assert response.json() == {"name": "test item"}