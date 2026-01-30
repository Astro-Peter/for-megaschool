"""
FastAPI Application Module
This module provides the main FastAPI application instance with basic endpoints.
"""

from fastapi import FastAPI
from typing import Dict, Any
from datetime import datetime

# Create the FastAPI app instance
app = FastAPI(
    title="Python Project Template API",
    description="A basic API endpoint for the Python Project Template",
    version="1.0.0"
)

@app.get("/")
async def root_endpoint() -> Dict[str, str]:
    """
    Root endpoint that returns a welcome message.
    """
    return {
        "message": "Welcome to the Python Project Template API!",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint that returns the status of the API.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "fastapi-api"
    }

@app.get("/info")
async def get_info() -> Dict[str, Any]:
    """
    Additional information endpoint.
    """
    return {
        "project": "Python Project Template",
        "framework": "FastAPI",
        "version": "1.0.0",
        "deployment_date": datetime.now().isoformat()
    }