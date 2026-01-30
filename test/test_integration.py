import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest

# There's nothing here yet!
import sys, os
import unittest
from fastapi.testclient import TestClient
from src.main import app

testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})

    def test_message(self):
        response = self.client.get("/message")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello from FastAPI!"})

if __name__ == '__main__':
    unittest.main()