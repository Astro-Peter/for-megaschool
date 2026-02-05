import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
from fastapi.testclient import TestClient
from src.modules.api import app


class TestAPIIntegration(unittest.TestCase):
    """Integration tests for the API"""
    
    def setUp(self):
        """Set up test client"""
        self.client = TestClient(app)

    def test_full_api_workflow(self):
        """Test a full workflow through multiple API endpoints"""
        # Test root endpoint
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
        # Test health endpoint
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        
        # Test calculate endpoint
        payload = {"value": 5.0, "unit": "metric"}
        response = self.client.post("/api/v1/calculate/gravity", json=payload)
        self.assertEqual(response.status_code, 200)
        
        # Verify the calculated result makes sense
        data = response.json()
        expected_force = payload["value"] * 9.81  # F = m * g
        self.assertAlmostEqual(data["result"], expected_force, places=2)
        
        # Test GET calculation endpoint
        response = self.client.get("/api/v1/calculate/earth-gravity/10.0")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()