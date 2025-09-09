import os
import pickle
import logging
from backend.core.config import settings



logger = logging.getLogger(__name__)

# Paths (relative to project root)
MODEL_DIR = settings.model_dir
MODEL_PATH = os.path.join(MODEL_DIR, settings.classifier_model)
VEC_PATH = os.path.join(MODEL_DIR, settings.vectorizer)

# Load model & vectorizer at import time
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(VEC_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    logger.info("Classifier and vectorizer loaded from %s", MODEL_DIR)
except Exception as e:
    logger.exception("Failed to load classifier/vectorizer from %s: %s", MODEL_DIR, str(e))
    model, vectorizer = None, None

def predict_document_type(text: str) -> str:
    """Classify OCR text into a document type."""
    if not text.strip():
        logger.warning("predict_document_type called with empty text")
        return "unknown"

    if not model or not vectorizer:
        logger.error("predict_document_type failed: model/vectorizer not loaded")
        return "unknown"

    try:
        logger.debug("Classifying text of length %d", len(text))
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]
        logger.info("Predicted document type: %s", prediction)
        return prediction
    except Exception as e:
        logger.exception("Classification failed: %s", str(e))
        return "unknown"
