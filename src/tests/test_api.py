import unittest
from fastapi.testclient import TestClient
from main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_item(self):
        response = self.client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1, "q": None})

    def test_create_item(self):
        response = self.client.post("/items/", json={"id": 1, "name": "Item 1", "price": 10.0})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "name": "Item 1", "price": 10.0})

if __name__ == '__main__':
    unittest.main()