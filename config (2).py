import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    gemini_api_key = os.getenv("GEMINI_API_KEY", "")
    gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
    cors_origins = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:8501,http://127.0.0.1:8501",
    )


settings = Settings()