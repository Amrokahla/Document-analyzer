import os
import logging

logger = logging.getLogger(__name__)

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_PATH = os.path.join(MODEL_DIR, "classifier_model.pkl")
VEC_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")


def check_liveness() -> dict:
    """Basic heartbeat — app is running."""
    logger.debug("Liveness check called")
    return {"status": "alive"}


def check_readiness() -> dict:
    """Deeper check — verify model/vectorizer exist."""
    logger.debug("Readiness check called")
    try:
        ready = os.path.exists(MODEL_PATH) and os.path.exists(VEC_PATH)
        status = "ready" if ready else "not ready"
        logger.info("Readiness check result: %s", status)
        return {
            "status": status,
            "model_path": MODEL_PATH,
            "vectorizer_path": VEC_PATH,
            "model_files_present": ready,
        }
    except Exception as e:
        logger.exception("Readiness check failed: %s", str(e))
        return {
            "status": "error",
            "error": str(e),
            "model_path": MODEL_PATH,
            "vectorizer_path": VEC_PATH,
            "model_files_present": False,
        }
