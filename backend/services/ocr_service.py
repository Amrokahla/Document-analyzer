import logging
from PIL import Image
import pytesseract
import io

logger = logging.getLogger(__name__)

def perform_ocr(file_bytes: bytes) -> str:
    """Run OCR on image bytes and return extracted text."""
    try:
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image)
        logger.info("OCR completed successfully, extracted %d characters", len(text))
        return text.strip()
    except Exception as e:
        logger.exception("OCR failed: %s", str(e))
        return f"OCR failed: {str(e)}"
