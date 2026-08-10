import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables"""
    api_title: str = "PDF Summarizer Agent"
    api_version: str = "1.0.0"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    max_file_size: int = 50 * 1024 * 1024  # 50MB
    allowed_extensions: list = [".pdf"]
    
    class Config:
        env_file = ".env"


settings = Settings()
