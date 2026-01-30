"""Health check router."""
from fastapi import APIRouter
from app.models import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify API functionality.

    Returns:
        HealthResponse: Status and message indicating API health
    """
    return HealthResponse(status="healthy", message="API is running")
