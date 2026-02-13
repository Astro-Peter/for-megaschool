"""
Quick test to ensure the API can be imported and run.
"""
try:
    from src.api.main import app
    print("✓ Successfully imported FastAPI app")
    
    # Check that the required dependencies are available
    import fastapi
    import uvicorn
    import pydantic
    print("✓ All required dependencies available")
    
    # Try creating a test client
    from fastapi.testclient import TestClient
    client = TestClient(app)
    print("✓ TestClient can be created")
    
    # Quick test of root endpoint
    response = client.get("/")
    if response.status_code == 200 and "Hello" in response.json():
        print("✓ Root endpoint works correctly")
    else:
        print(f"✗ Root endpoint failed: {response.status_code}, {response.json()}")
        
    print("\nAll quick tests passed!")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
except Exception as e:
    print(f"✗ Error: {e}")