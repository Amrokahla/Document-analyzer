import os
import pickle

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_PATH = os.path.join(MODEL_DIR, "trained_model.pkl")
VEC_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
with open(VEC_PATH, "rb") as f:
    vectorizer = pickle.load(f)

def predict_document_type(text: str) -> str:
    """Classify OCR text into a document type."""
    if not text.strip():
        return "unknown"
    X = vectorizer.transform([text])
    return model.predict(X)[0]
