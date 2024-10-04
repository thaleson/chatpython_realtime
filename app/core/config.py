# app/core/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if exists
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "Chat em Tempo Real com FastAPI"
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 8000))

settings = Settings()
