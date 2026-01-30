"""Health check response model."""
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""

    status: str
    message: str

    class Config:
        json_schema_extra = {
            "example": {"status": "healthy", "message": "API is running"}
        }
