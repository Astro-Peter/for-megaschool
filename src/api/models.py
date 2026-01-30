"""
Data models for the API
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class APIResponse(BaseModel):
    """
    Generic API Response model
    """
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None

class HealthCheck(BaseModel):
    """
    Health Check Response model
    """
    status: str = "healthy"
    details: Optional[Dict[str, Any]] = None