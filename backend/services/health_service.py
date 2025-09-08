import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_PATH = os.path.join(MODEL_DIR, "trained_model.pkl")
VEC_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")


def check_liveness() -> dict:
    """Basic heartbeat — app is running."""
    return {"status": "alive"}


def check_readiness() -> dict:
    """Deeper check — verify model/vectorizer exist."""
    ready = os.path.exists(MODEL_PATH) and os.path.exists(VEC_PATH)
    return {
        "status": "ready" if ready else "not ready",
        "model_path": MODEL_PATH,
        "vectorizer_path": VEC_PATH,
        "model_files_present": ready
    }
