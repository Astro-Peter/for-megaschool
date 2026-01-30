"""Health check endpoints."""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    message: str


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify API functionality.
    
    Returns:
        HealthResponse: Status and message indicating API is operational
    """
    return {
        "status": "healthy",
        "message": "API is running and operational"
    }
