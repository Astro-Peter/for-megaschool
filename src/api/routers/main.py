from fastapi import APIRouter
from typing import Optional
from ..models import HealthCheck, APIResponse

router = APIRouter()

@router.get("/health", response_model=HealthCheck)
async def health_check():
    """
    Simple health check endpoint
    """
    return HealthCheck(status="healthy")

@router.get("/status", response_model=APIResponse)
async def get_status():
    """
    Get service status information
    """
    return APIResponse(
        success=True,
        message="Service is operational"
    )

# Additional example endpoints
@router.get("/hello/{name}")
async def say_hello(name: str):
    """
    Example endpoint to demonstrate path parameters
    """
    return {"message": f"Hello, {name}!"}

@router.post("/echo")
async def echo_data(data: dict):
    """
    Example endpoint to demonstrate POST requests and data handling
    """
    return {"received": data, "status": "success"}