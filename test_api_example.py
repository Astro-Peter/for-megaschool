"""
Simple script to test that the API starts up correctly.
This can be used during development to verify basic API functionality.
"""

import subprocess
import time
import requests
import threading


def test_api_endpoints():
    """Test various API endpoints to ensure they're working."""
    base_url = "http://localhost:8000"
    
    # Test the root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"Root endpoint: {response.status_code}, Response: {response.json()}")
        assert response.status_code == 200
        assert "Hello" in response.json()
    except Exception as e:
        print(f"Error testing root endpoint: {e}")
    
    # Test the health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health endpoint: {response.status_code}, Response: {response.json()}")
        assert response.status_code == 200
        assert response.json().get("status") == "healthy"
    except Exception as e:
        print(f"Error testing health endpoint: {e}")
    
    # Test gravity endpoint (metric)
    try:
        response = requests.get(f"{base_url}/gravity/metric")
        print(f"Metric gravity endpoint: {response.status_code}, Response: {response.json()}")
        assert response.status_code == 200
        assert response.json()["gravity"] == 9.81
    except Exception as e:
        print(f"Error testing metric gravity endpoint: {e}")
    
    # Test gravity endpoint (imperial)
    try:
        response = requests.get(f"{base_url}/gravity/imperial")
        print(f"Imperial gravity endpoint: {response.status_code}, Response: {response.json()}")
        assert response.status_code == 200
        assert response.json()["gravity"] == 32.2
    except Exception as e:
        print(f"Error testing imperial gravity endpoint: {e}")


if __name__ == "__main__":
    print("Starting test of FastAPI endpoints...")
    
    # Start the API server in a separate thread/process
    import uvicorn
    from src.api.main import app
    import threading
    
    def run_server():
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    
    # Start server in background
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Wait a moment for server to start
    time.sleep(3)
    
    # Now run tests
    test_api_endpoints()
    
    print("API testing complete.")
    
    # Keep the script alive briefly so the server can be inspected if needed
    time.sleep(1)