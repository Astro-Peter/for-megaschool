# Health Check Setup Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the FastAPI Server
```bash
python main.py --mode server
```

### 3. Access the Health Check
```bash
curl http://localhost:8000/health
```

Or visit in your browser:
- Health Check: http://localhost:8000/health
- API Documentation: http://localhost:8000/docs

## What Was Implemented

### ✅ Core Features
- [x] Health check endpoint (`GET /health`)
- [x] Pydantic response model with proper schema
- [x] Component-based health checks (Python, System)
- [x] HTTP status code handling (200 for healthy, 503 for unhealthy)
- [x] Comprehensive test suite (17 tests)
- [x] Full API documentation
- [x] README with usage instructions

### ✅ Files Created/Modified

**New Files:**
- `src/modules/health.py` - Health check logic and response model
- `src/modules/app.py` - FastAPI application with endpoints
- `test/test_health.py` - Unit tests (17 test cases)
- `HEALTH_CHECK_API.md` - Complete API documentation
- `IMPLEMENTATION_SUMMARY.md` - Detailed implementation notes
- `HEALTHCHECK_SETUP_GUIDE.md` - This file

**Modified Files:**
- `src/main.py` - Added FastAPI server mode with command-line arguments
- `requirements.txt` - Added fastapi and uvicorn dependencies
- `README.md` - Added health check documentation and usage examples

## Test the Health Check

### Run Health Check Tests
```bash
python -m unittest test.test_health -v
```

### Run All Tests
```bash
python -m unittest discover -s test -p "test_*.py"
```

### Manual Testing with curl

**Test healthy endpoint:**
```bash
curl -v http://localhost:8000/health
```

**Expected response (HTTP 200):**
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

## Command-Line Options

### Start Server
```bash
python main.py --mode server
```

### Custom Host/Port
```bash
python main.py --mode server --host 0.0.0.0 --port 8080
```

### CLI Mode (Default)
```bash
python main.py
```

### Help
```bash
python main.py --help
```

## API Endpoints

### GET /
Root endpoint with welcome message
- **Response:** JSON with welcome message

### GET /health
Health check endpoint
- **Status Code:** 200 (healthy) or 503 (unhealthy)
- **Response:** HealthCheckResponse JSON

### GET /docs
Interactive API documentation (Swagger UI)

### GET /redoc
Alternative API documentation (ReDoc)

## Health Check Response Fields

```json
{
  "status": "healthy|unhealthy",
  "timestamp": "2024-01-15T10:30:45.123456",
  "version": "1.0.0",
  "checks": {
    "python": true|false,
    "system": true|false
  }
}
```

### Field Descriptions
- **status**: Overall health status - "healthy" if all checks pass, "unhealthy" otherwise
- **timestamp**: ISO 8601 UTC timestamp when check was performed
- **version**: Application version string
- **checks**: Object containing individual component check results

## Integration Examples

### Docker
Add to Dockerfile:
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1
```

### Kubernetes
Add to deployment YAML:
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

### Python Script
```python
import requests

response = requests.get('http://localhost:8000/health')
if response.status_code == 200:
    health_data = response.json()
    print(f"Status: {health_data['status']}")
    print(f"Version: {health_data['version']}")
else:
    print("Application is unhealthy")
```

### Bash Script
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

## Extending the Health Check

To add more component checks:

1. **Edit `src/modules/health.py`:**
   ```python
   def _checkDatabase(self) -> bool:
       """Check database connectivity."""
       try:
           # Your check logic here
           return True
       except Exception:
           return False
   ```

2. **Add to `_performComponentChecks()` method:**
   ```python
   def _performComponentChecks(self) -> Dict[str, bool]:
       return {
           "python": self._checkPython(),
           "system": self._checkSystem(),
           "database": self._checkDatabase(),  # New check
       }
   ```

3. **Add tests to `test/test_health.py`:**
   ```python
   def test_health_checker_database_check(self):
       """Test database component check."""
       result = self.checker.checkApplicationHealth()
       self.assertIn("database", result.checks)
   ```

## Troubleshooting

### Server Won't Start
- Ensure port 8000 is not in use
- Try: `python main.py --mode server --port 8080`
- Check that fastapi and uvicorn are installed: `pip install -r requirements.txt`

### Health Check Returns 503
- Check which components are failing in the response
- Verify Python version is 3.7+: `python --version`
- Check application logs for error messages

### Import Errors
- Make sure you're running from the project root directory
- Verify PYTHONPATH includes the src directory
- Reinstall dependencies: `pip install -r requirements.txt`

## Documentation Files

- **HEALTH_CHECK_API.md** - Comprehensive API documentation
- **IMPLEMENTATION_SUMMARY.md** - Implementation details and compliance
- **HEALTHCHECK_SETUP_GUIDE.md** - This guide
- **README.md** - Project overview with health check section

## Standards and Conventions

This implementation follows:
- **PEP 8** - Python style guide
- **FastAPI best practices** - Modern async Python web framework patterns
- **Pydantic validation** - Type-safe data validation
- **unittest framework** - Python standard testing library

## Next Steps

1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python main.py --mode server`
3. Visit documentation: http://localhost:8000/docs
4. Check health: http://localhost:8000/health
5. Run tests: `python -m unittest test.test_health -v`

## Support

For more information:
- See **HEALTH_CHECK_API.md** for comprehensive API documentation
- See **IMPLEMENTATION_SUMMARY.md** for implementation details
- See **README.md** for general project information
