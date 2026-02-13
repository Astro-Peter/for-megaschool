"""FastAPI application factory."""
import logging
from fastapi import FastAPI
from app.config import Settings
from app.routers import health_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app(settings: Settings) -> FastAPI:
    """
    Create and configure the FastAPI application.

    Args:
        settings: Application settings instance

    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOC_URL,
        openapi_url=settings.OPENAPI_URL,
    )

    # Register event handlers
    @app.on_event("startup")
    async def startup_event():
        """Run on application startup."""
        logger.info(f"🚀 Starting {settings.APP_NAME} v{settings.APP_VERSION}")

    @app.on_event("shutdown")
    async def shutdown_event():
        """Run on application shutdown."""
        logger.info(f"🛑 Shutting down {settings.APP_NAME}")

    # Include routers
    app.include_router(health_router)

    return app
