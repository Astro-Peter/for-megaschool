# FastAPI Quick Start Guide

## Installation & Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cd src
cp .env.TEMPLATE .env
# Edit .env if needed (defaults should work for local development)
```

### 3. Start Development Server
```bash
uvicorn api:app --reload
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started server process [12345]
INFO:     Application startup complete
🚀 FastAPI Application v0.1.0 starting up...
📝 Debug mode: False
```

## Access Your API

Open your browser and navigate to:

- **API Documentation**: http://localhost:8000/docs (Interactive Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc (ReDoc)
- **Health Check**: http://localhost:8000/api/health
- **API Root**: http://localhost:8000

## Test the API

### Using cURL
```bash
# Health check
curl http://localhost:8000/api/health

# Root endpoint
curl http://localhost:8000/
```

### Using Python
```python
import requests

# Health check
response = requests.get("http://localhost:8000/api/health")
print(response.json())

# Root endpoint
response = requests.get("http://localhost:8000/")
print(response.json())
```

## Project Structure

```
src/app/
├── main.py              # FastAPI app setup and configuration
├── config/
│   └── settings.py      # Environment variables and settings
├── routers/
│   └── health.py        # Health check endpoint (example)
└── models/              # Pydantic data models (empty template)
```

## Adding Your First Endpoint

### 1. Create a router file: `src/app/routers/items.py`
```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float


@router.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get an item by ID."""
    return {"item_id": item_id, "name": "Example Item", "price": 9.99}


@router.post("/items", response_model=Item)
async def create_item(item: Item):
    """Create a new item."""
    return item
```

### 2. Register the router in `src/app/main.py`
```python
from app.routers import health, items

# In create_app() function, add:
app.include_router(items.router, prefix=settings.API_PREFIX, tags=["items"])
```

### 3. Test your endpoint
- Visit: http://localhost:8000/docs
- Try the new `/api/items` endpoints
- The docs update automatically!

## Key Features

✅ **Auto-reloading**: Server reloads on code changes  
✅ **Type hints**: Full IDE support and validation  
✅ **Interactive docs**: Swagger UI at `/docs`  
✅ **CORS enabled**: Ready for frontend integration  
✅ **Environment config**: Manage settings via `.env`  
✅ **Logging**: Rich logging with emoji support  
✅ **Pydantic models**: Automatic request/response validation  

## Common Commands

```bash
# Run with auto-reload (development)
uvicorn api:app --reload

# Run with specific host/port
uvicorn api:app --host 0.0.0.0 --port 8000

# Run without auto-reload (production-like)
uvicorn api:app --reload=false

# Access different ports
uvicorn api:app --port 8080
```

## Environment Variables

Located in `src/.env`:

```env
APP_NAME=FastAPI Application
APP_VERSION=0.1.0
DEBUG=False              # Set to True for verbose logging
HOST=0.0.0.0
PORT=8000
ALLOWED_ORIGINS=http://localhost,http://localhost:3000
```

## Troubleshooting

**Port already in use?**
```bash
# Use a different port
uvicorn api:app --port 8080
```

**Import errors?**
```bash
# Make sure you're in the src directory or have src in PYTHONPATH
cd src
uvicorn api:app --reload

# OR from project root:
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
uvicorn src.api:app --reload
```

**Need to reload docs?**
- Hard refresh your browser (Ctrl+Shift+R or Cmd+Shift+R)
- The OpenAPI schema is cached by the browser

## Next Steps

1. Read the full [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for detailed information
2. Check FastAPI docs: https://fastapi.tiangolo.com/
3. Add more routers and endpoints as needed
4. Consider adding database models and queries
5. Implement authentication and authorization
6. Deploy to your preferred hosting platform

Happy coding! 🚀
