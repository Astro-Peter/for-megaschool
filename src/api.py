"""FastAPI development entry point.

This file is the main entry point for running the FastAPI application
using uvicorn during development.

To run the development server:
    uvicorn src.api:app --reload
"""
from app.main import app

if __name__ == "__main__":
    import uvicorn
    from app.config.settings import settings
    
    uvicorn.run(
        "api:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
