"""FastAPI application initialization and configuration."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.routers import health
from modules.logger import Log

# Initialize logger
log = Log()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for application startup and shutdown events.
    
    Args:
        app: FastAPI application instance
        
    Yields:
        None
    """
    # Startup event
    log.success(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION} starting up...")
    log.info(f"📝 Debug mode: {settings.DEBUG}")
    yield
    
    # Shutdown event
    log.info(f"🛑 {settings.APP_NAME} shutting down...")


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        lifespan=lifespan
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    app.include_router(health.router, prefix=settings.API_PREFIX, tags=["health"])
    
    # Root endpoint
    @app.get("/")
    async def root():
        """Root endpoint returning API information."""
        return {
            "message": f"Welcome to {settings.APP_NAME}",
            "version": settings.APP_VERSION,
            "docs": "/docs",
            "health": f"{settings.API_PREFIX}/health"
        }
    
    log.debug("✅ FastAPI application configured successfully")
    return app


# Create the application instance
app = create_app()
