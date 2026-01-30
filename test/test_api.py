import sys, os
import unittest

# Add src to path for imports
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

try:
    from fastapi.testclient import TestClient
    from api.main import app
except ImportError as e:
    print(f"Error importing API components: {e}")
    print("Make sure you've installed the required dependencies with: pip install -r requirements.txt")
    raise e

class TestAPI(unittest.TestCase):
    def setUp(self):
        """Set up test client for each test"""
        self.client = TestClient(app)

    def test_root_endpoint(self):
        """Test the root endpoint returns correct response"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "FastAPI service is running!"})

    def test_health_endpoint(self):
        """Test the health endpoint returns healthy status"""
        response = self.client.get("/api/v1/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})

    def test_status_endpoint(self):
        """Test the status endpoint returns success status"""
        response = self.client.get("/api/v1/status")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        self.assertEqual(data["message"], "Service is operational")

    def test_hello_endpoint(self):
        """Test the hello endpoint with a sample name"""
        response = self.client.get("/api/v1/hello/testuser")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, testuser!"})

    def test_echo_endpoint(self):
        """Test the echo endpoint with sample data"""
        test_data = {"key": "value", "number": 123}
        response = self.client.post("/api/v1/echo", json=test_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["received"], test_data)
        self.assertEqual(response_data["status"], "success")

if __name__ == '__main__':
    unittest.main()