"""
FastAPI application module.
Sets up the FastAPI application with health check endpoint and other configurations.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from modules.health import HealthChecker, HealthCheckResponse
from modules.logger import Log

# Initialize logger
log = Log()

# Create FastAPI app instance
app = FastAPI(
    title="Python Project API",
    description="API with health check endpoint",
    version="1.0.0"
)

# Initialize health checker
health_checker = HealthChecker(version="1.0.0")


@app.get("/health", response_model=HealthCheckResponse)
async def getHealthStatus():
    """
    Health check endpoint to monitor application status and availability.
    
    Returns:
        HealthCheckResponse with application status, timestamp, version, and component checks
        - Status Code 200: Application is healthy
        - Status Code 503: Application is unhealthy (at least one component failed)
    """
    health_response = health_checker.checkApplicationHealth()
    
    # Return 503 Service Unavailable if not healthy
    if health_response.status != "healthy":
        return JSONResponse(
            status_code=503,
            content=health_response.dict()
        )
    
    # Return 200 OK if healthy
    return JSONResponse(
        status_code=200,
        content=health_response.dict()
    )


@app.get("/")
async def getRoot():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to the Python Project API. Visit /health for health status or /docs for API documentation."}
