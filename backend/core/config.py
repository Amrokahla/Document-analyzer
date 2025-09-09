# backend/core/config.py
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

class Settings(BaseSettings):
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    model_dir: str = os.getenv("MODEL_DIR", "backend/model")
    classifier_model: str = os.getenv("CLASSIFIER_MODEL", "classifier_model.pkl")
    vectorizer: str = os.getenv("VECTORIZER", "vectorizer.pkl")
    ocr_lang: str = os.getenv("OCR_LANG", "eng")

settings = Settings()
