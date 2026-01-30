from fastapi import FastAPI
import time
from typing import Optional

# Import existing functionality from the main app if needed
from src.modules.logger import Log
from pydantic import BaseModel

# Initialize the app
app = FastAPI(
    title="Python Project API",
    description="API for the Python project boilerplate",
    version="1.0.0"
)

# Example data model
class Message(BaseModel):
    text: str
    timestamp: Optional[float] = None


# CONSTANTS
GRAVITY_METRIC = 9.81  # m/s^2
GRAVITY_IMPERIAL = 32.2  # ft/s^2

# Logging instance
log = Log()


@app.get("/")
def read_root():
    """Root endpoint for the API."""
    log.info("Root endpoint accessed")
    return {"Hello": "World", "status": "API is running successfully"}


@app.get("/health")
def health_check():
    """Health check endpoint to verify API is operational."""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "service": "python-project-api"
    }


@app.get("/gravity/{unit}")
def get_gravity(unit: str = "metric"):
    """
    Get gravity constant value based on unit system.
    
    Args:
        unit (str): "metric" for m/s² or "imperial" for ft/s²
    
    Returns:
        dict: Gravity value and unit
    """
    if unit.lower() == "imperial":
        return {"gravity": GRAVITY_IMPERIAL, "unit": "ft/s²"}
    else:  # default to metric
        return {"gravity": GRAVITY_METRIC, "unit": "m/s²"}


@app.post("/message")
def post_message(message: Message):
    """
    Accept and echo back a message.
    
    Args:
        message (Message): Input message containing text
    
    Returns:
        dict: Echo of the input message with timestamp
    """
    if not message.timestamp:
        message.timestamp = time.time()
        
    response = {
        "received_message": message.text,
        "timestamp": message.timestamp,
        "echo_back": f"Echo: {message.text}",
    }
    
    log.info(f"Message received: {message.text}")
    return response


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """
    Example endpoint showing URL parameters and query parameters.
    
    Args:
        item_id (int): Item identifier from URL path
        q (str, optional): Query parameter
    
    Returns:
        dict: Item information with optional query parameter
    """
    result = {"item_id": item_id}
    
    if q:
        result["query"] = q
        result["description"] = f"Item {item_id} with query {q}"
    else:
        result["description"] = f"Item {item_id}"
    
    return result


if __name__ == "__main__":
    import uvicorn
    # For development/testing only
    uvicorn.run(app, host="0.0.0.0", port=8000)