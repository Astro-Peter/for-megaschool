# FastAPI Application Documentation

## Overview

This project includes a modern FastAPI-based REST API with a clean, organized project structure. FastAPI automatically generates interactive API documentation and is built on top of Starlette and Pydantic.

## Project Structure

```
src/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application initialization
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py      # Configuration management
│   ├── routers/
│   │   ├── __init__.py
│   │   └── health.py        # Health check endpoints
│   └── models/
│       └── __init__.py      # Data models (Pydantic schemas)
├── api.py                   # Development entry point
└── modules/
    └── logger.py            # Logging utilities
```

## Getting Started

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cd src
cp .env.TEMPLATE .env
# Edit .env with your configuration
```

### Running the Development Server

```bash
cd src
uvicorn api:app --reload
```

The `--reload` flag enables auto-reload when you make code changes.

### Accessing the API

- **API Base URL**: `http://localhost:8000`
- **Interactive Docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative Docs (ReDoc)**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

## API Endpoints

### Health Check

#### GET `/api/health`

Health check endpoint to verify API functionality.

**Response:**
```json
{
  "status": "healthy",
  "message": "API is running and operational"
}
```

### Root

#### GET `/`

Returns API information and available endpoints.

**Response:**
```json
{
  "message": "Welcome to FastAPI Application",
  "version": "0.1.0",
  "docs": "/docs",
  "health": "/api/health"
}
```

## Configuration

Application configuration is managed through environment variables defined in the `.env` file.

### Available Settings

- `APP_NAME` (default: "FastAPI Application") - Application name
- `APP_VERSION` (default: "0.1.0") - Application version
- `DEBUG` (default: "False") - Enable debug mode
- `HOST` (default: "0.0.0.0") - Server host
- `PORT` (default: "8000") - Server port
- `ALLOWED_ORIGINS` (default: "http://localhost,http://localhost:3000") - CORS allowed origins (comma-separated)

## Adding New Endpoints

### 1. Create a Router

Create a new file in `src/app/routers/`:

```python
# src/app/routers/users.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    id: int
    name: str
    email: str


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Get a user by ID."""
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}


@router.post("/users", response_model=User)
async def create_user(user: User):
    """Create a new user."""
    return user
```

### 2. Register the Router

Update `src/app/main.py`:

```python
from app.routers import health, users

# In create_app() function:
app.include_router(health.router, prefix=settings.API_PREFIX, tags=["health"])
app.include_router(users.router, prefix=settings.API_PREFIX, tags=["users"])
```

## Creating Data Models

Define Pydantic models in `src/app/models/`:

```python
# src/app/models/user.py
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
```

## Middleware & Event Handlers

The application includes:

- **CORS Middleware**: Handles cross-origin requests
- **Lifespan Context Manager**: Manages application startup and shutdown events

### Startup/Shutdown Events

Events are handled in the `lifespan` context manager in `src/app/main.py`:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    log.success("🚀 Application starting up...")
    yield
    # Shutdown
    log.info("🛑 Application shutting down...")
```

## Logging

The application uses the `Rich` library for enhanced logging. Access the logger via:

```python
from modules.logger import Log

log = Log()
log.success("Success message")
log.info("Info message")
log.debug("Debug message")
log.hbar("Section Header")
```

## Development Best Practices

1. **Type Hints**: Always use type hints for better code clarity and IDE support
2. **Pydantic Models**: Use Pydantic models for request/response validation
3. **Async Functions**: Use `async` functions for better performance
4. **Documentation**: Add docstrings to all endpoints
5. **Error Handling**: Use HTTPException for API errors
6. **Environment Variables**: Store all configuration in `.env`

## Deployment

### Using Gunicorn with Uvicorn Workers

```bash
gunicorn src.api:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

## Testing

Create tests in the `test/` directory:

```python
# test/test_health.py
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

Run tests:

```bash
python -m pytest test/
```

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Starlette Documentation](https://www.starlette.io/)
