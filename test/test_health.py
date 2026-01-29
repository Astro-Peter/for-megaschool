"""
Unit tests for the health check endpoint.
"""

import sys
import os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from src.modules.app import app
from src.modules.health import HealthChecker, HealthCheckResponse


class TestHealthCheckEndpoint(unittest.TestCase):
    """Test cases for the health check endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = TestClient(app)

    def test_health_endpoint_returns_200_when_healthy(self):
        """Test that /health endpoint returns 200 status code when application is healthy."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_health_endpoint_returns_valid_response_structure(self):
        """Test that /health endpoint returns valid response structure."""
        response = self.client.get("/health")
        data = response.json()
        
        # Check required fields
        self.assertIn("status", data)
        self.assertIn("timestamp", data)
        self.assertIn("version", data)
        self.assertIn("checks", data)

    def test_health_endpoint_status_field_is_healthy(self):
        """Test that status field indicates healthy when all checks pass."""
        response = self.client.get("/health")
        data = response.json()
        
        self.assertEqual(data["status"], "healthy")

    def test_health_endpoint_version_is_present(self):
        """Test that version is included in response."""
        response = self.client.get("/health")
        data = response.json()
        
        self.assertIsNotNone(data["version"])
        self.assertEqual(data["version"], "1.0.0")

    def test_health_endpoint_timestamp_is_present(self):
        """Test that timestamp is included in response."""
        response = self.client.get("/health")
        data = response.json()
        
        self.assertIsNotNone(data["timestamp"])

    def test_health_endpoint_checks_include_components(self):
        """Test that checks include component status."""
        response = self.client.get("/health")
        data = response.json()
        
        checks = data["checks"]
        self.assertIsInstance(checks, dict)
        self.assertIn("python", checks)
        self.assertIn("system", checks)

    def test_root_endpoint_returns_welcome_message(self):
        """Test that root endpoint returns welcome message."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        self.assertIn("Welcome", data["message"])


class TestHealthChecker(unittest.TestCase):
    """Test cases for the HealthChecker class."""

    def setUp(self):
        """Set up test fixtures."""
        self.checker = HealthChecker(version="1.0.0")

    def test_health_checker_returns_response_object(self):
        """Test that checkApplicationHealth returns HealthCheckResponse object."""
        result = self.checker.checkApplicationHealth()
        self.assertIsInstance(result, HealthCheckResponse)

    def test_health_checker_includes_required_fields(self):
        """Test that health check response includes all required fields."""
        result = self.checker.checkApplicationHealth()
        
        self.assertIsNotNone(result.status)
        self.assertIsNotNone(result.timestamp)
        self.assertIsNotNone(result.version)
        self.assertIsNotNone(result.checks)

    def test_health_checker_status_is_healthy_by_default(self):
        """Test that status is healthy when all component checks pass."""
        result = self.checker.checkApplicationHealth()
        self.assertEqual(result.status, "healthy")

    def test_health_checker_version_matches_input(self):
        """Test that version in response matches initialized version."""
        custom_version = "2.5.3"
        checker = HealthChecker(version=custom_version)
        result = checker.checkApplicationHealth()
        
        self.assertEqual(result.version, custom_version)

    def test_health_checker_python_check_passes(self):
        """Test that Python component check passes."""
        result = self.checker.checkApplicationHealth()
        
        self.assertTrue(result.checks["python"])

    def test_health_checker_system_check_passes(self):
        """Test that system component check passes."""
        result = self.checker.checkApplicationHealth()
        
        self.assertTrue(result.checks["system"])


class TestHealthCheckResponse(unittest.TestCase):
    """Test cases for the HealthCheckResponse model."""

    def test_health_check_response_can_be_serialized(self):
        """Test that HealthCheckResponse can be serialized to dict."""
        from datetime import datetime
        
        response = HealthCheckResponse(
            status="healthy",
            timestamp=datetime.utcnow(),
            version="1.0.0",
            checks={"python": True, "system": True}
        )
        
        data = response.dict()
        self.assertIsInstance(data, dict)
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["version"], "1.0.0")

    def test_health_check_response_requires_status(self):
        """Test that HealthCheckResponse requires status field."""
        from datetime import datetime
        
        with self.assertRaises(TypeError):
            HealthCheckResponse(
                timestamp=datetime.utcnow(),
                version="1.0.0",
                checks={}
            )

    def test_health_check_response_requires_timestamp(self):
        """Test that HealthCheckResponse requires timestamp field."""
        with self.assertRaises(TypeError):
            HealthCheckResponse(
                status="healthy",
                version="1.0.0",
                checks={}
            )


if __name__ == '__main__':
    unittest.main()
