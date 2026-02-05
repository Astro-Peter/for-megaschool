import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
from src.main import testFunction
from fastapi.testclient import TestClient
from src.modules.api import app


class TestSum(unittest.TestCase):
    def test_testFunction(self):
        """
        Test that it can sum a list of integers
        """
        self.assertTrue(testFunction())


class TestAPIEndpoints(unittest.TestCase):
    """API-specific tests"""
    
    def setUp(self):
        """Set up test client"""
        self.client = TestClient(app)
        
    def test_root_endpoint(self):
        """Test the root endpoint"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        self.assertIn("project", data)
        self.assertEqual(data["message"], "Welcome to the project API!")
        
    def test_health_endpoint(self):
        """Test the health endpoint"""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("status", data)
        self.assertIn("uptime", data)
        self.assertIn("version", data)
        self.assertEqual(data["status"], "healthy")
        
    def test_status_endpoint(self):
        """Test the status endpoint"""
        response = self.client.get("/api/v1/status")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "API is running")
        self.assertEqual(data["data"]["status"], "active")
        
    def test_process_endpoint(self):
        """Test the process endpoint"""
        payload = {"message": "test data", "data": {"key": "value"}}
        response = self.client.post("/api/v1/process", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "Data processed successfully")
        self.assertEqual(data["data"]["message"], payload["message"])
        
    def test_calculate_gravity_endpoint(self):
        """Test the gravity calculation endpoint"""
        payload = {"value": 10.0, "unit": "metric"}
        response = self.client.post("/api/v1/calculate/gravity", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "Calculated force using metric units")
        self.assertIn("result", data)
        expected_result = payload["value"] * 9.81  # mass * gravity
        self.assertAlmostEqual(data["result"], expected_result, places=2)
        
    def test_get_earth_gravity_endpoint(self):
        """Test the earth gravity calculation endpoint (GET)"""
        mass = 10.0
        response = self.client.get(f"/api/v1/calculate/earth-gravity/{mass}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn(f"Earth gravity force calculated for mass {mass}", data["message"])
        self.assertIn("result", data)
        expected_result = mass * 9.81  # mass * gravity
        self.assertAlmostEqual(data["result"], expected_result, places=2)


if __name__ == '__main__':
    unittest.main()

# Additional test to make sure the import works properly
def test_api_can_be_imported(self):
    """Test that API module can be imported without errors"""
    from src.modules.api import app
    self.assertIsNotNone(app)