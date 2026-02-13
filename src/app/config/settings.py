"""Application configuration settings."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""
    
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Application")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    API_PREFIX: str = "/api"
    
    # Server settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # CORS settings
    ALLOWED_ORIGINS: list = os.getenv(
        "ALLOWED_ORIGINS", 
        "http://localhost,http://localhost:3000"
    ).split(",")


settings = Settings()
