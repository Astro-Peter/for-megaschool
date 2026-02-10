# Health Check API Documentation

This document describes the health check endpoint and how to use it for monitoring application status and availability.

## Overview

The FastAPI application includes a health check endpoint that allows you to monitor the application's status and verify that critical system components are functioning correctly.

## Running the FastAPI Server

To start the FastAPI server with the health check endpoint:

```bash
python main.py --mode server
```

Or with custom host and port:

```bash
python main.py --mode server --host 0.0.0.0 --port 8000
```

## Health Check Endpoint

### Endpoint Details

- **Path:** `/health`
- **Method:** `GET`
- **Response Type:** JSON
- **Response Model:** `HealthCheckResponse`

### Request

```bash
curl http://localhost:8000/health
```

### Response

#### Healthy Response (Status Code: 200)

```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:45.123456",
  "version": "1.0.0",
  "checks": {
    "python": true,
    "system": true
  }
}
```

#### Unhealthy Response (Status Code: 503)

```json
{
  "status": "unhealthy",
  "timestamp": "2024-01-15T10:30:45.123456",
  "version": "1.0.0",
  "checks": {
    "python": false,
    "system": true
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Overall health status: `"healthy"` or `"unhealthy"` |
| `timestamp` | ISO 8601 datetime | UTC timestamp of when the health check was performed |
| `version` | string | Application version |
| `checks` | object | Object containing individual component health checks |

### Component Checks

The `checks` object contains the status of individual system components:

| Component | Description |
|-----------|-------------|
| `python` | Python runtime version check (requires Python 3.7+) |
| `system` | Basic system responsiveness check |

## HTTP Status Codes

| Code | Description |
|------|-------------|
| `200` | Application is healthy (all component checks passed) |
| `503` | Service Unavailable - Application is unhealthy (at least one component check failed) |

## Usage Examples

### Check Application Health

```bash
curl -X GET http://localhost:8000/health
```

### Check Health with Verbose Output

```bash
curl -v http://localhost:8000/health
```

### Using in Scripts

**Python:**
```python
import requests

response = requests.get('http://localhost:8000/health')
if response.status_code == 200:
    print("Application is healthy")
else:
    print("Application is unhealthy")
    print(response.json())
```

**Bash:**
```bash
#!/bin/bash

STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health)

if [ $STATUS -eq 200 ]; then
    echo "Application is healthy"
    exit 0
else
    echo "Application is unhealthy (HTTP $STATUS)"
    exit 1
fi
```

### Docker Health Check

For use in Docker containers, you can add a health check to your Dockerfile:

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1
```

### Kubernetes Liveness Probe

For use in Kubernetes deployments:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 10
```

## Interactive API Documentation

When the FastAPI server is running, you can access the interactive API documentation:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Testing the Health Check

Run the health check tests:

```bash
python -m unittest test.test_health
```

For more detailed test output:

```bash
python -m unittest test.test_health -v
```

## Monitoring and Alerting

The health check endpoint is designed to be used with monitoring and alerting systems:

### Example: Monitoring with Prometheus

Configure Prometheus to scrape the health check endpoint and set up alerts for when the status code is not 200.

### Example: Monitoring with Datadog

Use Datadog's HTTP checks to monitor the `/health` endpoint and receive alerts when the application becomes unhealthy.

### Example: Monitoring with New Relic

Use New Relic's synthetic monitoring to periodically check the `/health` endpoint.

## Extending the Health Check

To add additional component checks, edit `src/modules/health.py`:

1. Add a new private method `_checkComponentName()` to the `HealthChecker` class
2. Add the check to the `_performComponentChecks()` method
3. Add corresponding unit tests to `test/test_health.py`

Example:

```python
def _checkDatabase(self) -> bool:
    """Check database connectivity."""
    try:
        # Your database connection logic here
        return True
    except Exception:
        return False
```

Then add it to `_performComponentChecks()`:

```python
def _performComponentChecks(self) -> Dict[str, bool]:
    return {
        "python": self._checkPython(),
        "system": self._checkSystem(),
        "database": self._checkDatabase(),  # New check
    }
```

## Best Practices

1. **Use appropriate HTTP status codes:** Return 200 for healthy and 503 for unhealthy
2. **Include timestamps:** Helps with debugging and monitoring
3. **Keep it lightweight:** Health checks should be fast and not consume significant resources
4. **Monitor regularly:** Set up automated monitoring to check the health endpoint periodically
5. **Log failures:** Log component check failures for debugging and alerting
6. **Document components:** Keep documentation of all component checks current
7. **Test thoroughly:** Write unit tests for all component checks

## Troubleshooting

### Health check returns 503

1. Check which components are failing by examining the `checks` object
2. Review application logs for error messages
3. Verify all required services are running
4. Check Python version is 3.7 or higher

### Health check endpoint is not responding

1. Verify the FastAPI server is running: `python main.py --mode server`
2. Check the server is listening on the correct host and port
3. Verify there are no firewall issues blocking the connection
4. Check application logs for startup errors

## Support

For issues or questions about the health check endpoint, please refer to the main README.md or contact the project maintainers.
