from pydantic import BaseSettings

class Settings(BaseSettings):
    environment: str = "development"
    port: int = 8000

    class Config:
        env_file = '.env'

settings = Settings()