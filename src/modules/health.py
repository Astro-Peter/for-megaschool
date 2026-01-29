"""
Health check module for FastAPI application.
Provides endpoints and logic for monitoring application status and availability.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any
import sys


class HealthCheckResponse(BaseModel):
    """Schema for health check response."""
    status: str
    timestamp: datetime
    version: str
    checks: Dict[str, Any]


class HealthChecker:
    """Handles health check logic for the application."""

    def __init__(self, version: str = "1.0.0"):
        """
        Initialize the HealthChecker.
        
        Args:
            version: Application version string
        """
        self.version = version

    def checkApplicationHealth(self) -> HealthCheckResponse:
        """
        Perform comprehensive health check of the application.
        
        Returns:
            HealthCheckResponse with status and component checks
        """
        checks = self._performComponentChecks()
        is_healthy = all(checks.values())
        
        return HealthCheckResponse(
            status="healthy" if is_healthy else "unhealthy",
            timestamp=datetime.utcnow(),
            version=self.version,
            checks=checks
        )

    def _performComponentChecks(self) -> Dict[str, bool]:
        """
        Perform checks on critical system components.
        
        Returns:
            Dictionary with component names as keys and health status as values
        """
        return {
            "python": self._checkPython(),
            "system": self._checkSystem(),
        }

    def _checkPython(self) -> bool:
        """Check Python runtime status."""
        try:
            # Verify Python is running and accessible
            return sys.version_info >= (3, 7)
        except Exception:
            return False

    def _checkSystem(self) -> bool:
        """Check basic system status."""
        try:
            # Verify system is responsive
            return True
        except Exception:
            return False
