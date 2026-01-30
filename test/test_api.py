import unittest
from fastapi.testclient import TestClient
from src.api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_user(self):
        response = self.client.post("/users/", json={"id": 1, "name": "John Doe", "email": "johndoe@example.com"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "name": "John Doe", "email": "johndoe@example.com"})

    def test_get_user(self):
        response = self.client.get("/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "name": "Sample User", "email": "sample@example.com"})