"""FastAPI application entry point."""
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from app.config import settings

# Create the FastAPI application
app = create_app(settings)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        log_level="info",
    )
