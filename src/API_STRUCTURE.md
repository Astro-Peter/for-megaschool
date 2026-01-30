# FastAPI Application Structure

This document describes the structure and organization of the FastAPI application.

## Project Structure

```
src/
├── api.py                 # FastAPI application entry point
├── app/                   # Main application package
│   ├── __init__.py        # Application factory (create_app function)
│   ├── config/            # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py    # Settings loaded from environment variables
│   ├── models/            # Pydantic data models
│   │   ├── __init__.py
│   │   └── health.py      # Health check response model
│   └── routers/           # API route handlers
│       ├── __init__.py
│       └── health.py      # Health check endpoint
├── main.py                # Original CLI application entry point
└── modules/               # Utility modules
    ├── __init__.py
    └── logger.py          # Logging utilities
```

## File Descriptions

### `api.py`
The entry point for running the FastAPI server. It:
- Imports and initializes the FastAPI app using the factory function
- Loads configuration from environment variables
- Provides Uvicorn configuration for running the development server

**To run the server:**
```bash
cd src
python api.py
```

Or use Uvicorn directly:
```bash
cd src
uvicorn api:app --reload
```

### `app/__init__.py`
Contains the `create_app()` factory function that:
- Creates the FastAPI application instance
- Registers startup and shutdown event handlers
- Includes route routers
- Configures API documentation

### `app/config/settings.py`
Manages application configuration:
- Loads environment variables from `.env` file
- Provides typed access to configuration values
- Defaults are provided for all settings

**Available settings:**
- `APP_NAME`: Application name
- `APP_VERSION`: Application version
- `APP_DESCRIPTION`: Application description
- `DEBUG`: Debug mode flag
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `RELOAD`: Auto-reload on code changes

### `app/models/health.py`
Defines Pydantic data models:
- `HealthResponse`: Response model for the health check endpoint

These models provide:
- Type validation and serialization
- Automatic OpenAPI schema generation
- JSON schema examples

### `app/routers/health.py`
Defines API endpoints:
- `GET /health`: Health check endpoint that returns API status

### `src/.env.TEMPLATE`
Template for environment variables. Copy to `.env` and update values.

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment:**
   ```bash
   cd src
   cp .env.TEMPLATE .env
   # Edit .env with your configuration
   ```

3. **Run the development server:**
   ```bash
   cd src
   python api.py
   ```

4. **Access the API:**
   - Main API: http://localhost:8000
   - Swagger UI docs: http://localhost:8000/docs
   - ReDoc docs: http://localhost:8000/redoc
   - Health check: http://localhost:8000/health

## Adding New Endpoints

To add a new endpoint:

1. Create a new router file in `app/routers/` (e.g., `app/routers/users.py`)
2. Define your endpoints using FastAPI decorators
3. Import and include the router in `app/__init__.py`:
   ```python
   from app.routers import users_router
   app.include_router(users_router)
   ```

## Adding New Models

To add new data models:

1. Create model files in `app/models/` (e.g., `app/models/user.py`)
2. Define your Pydantic models
3. Import and export in `app/models/__init__.py`
4. Use in your routers for request/response validation

## Configuration via Environment Variables

Edit `src/.env` to configure:
```
APP_NAME=My API
APP_VERSION=1.0.0
DEBUG=True
PORT=8000
```

All settings are optional and have sensible defaults.
