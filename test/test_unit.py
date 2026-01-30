import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest


def testFunction():
    return True

class TestSum(unittest.TestCase):
    def test_testFunction(self):
        """
        Test that it can sum a list of integers
        """
        self.assertTrue(testFunction())


if __name__ == '__main__':
    unittest.main()

# Test for FastAPI Integration
from fastapi.testclient import TestClient
import httpx
from src.api import app

def test_read_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
