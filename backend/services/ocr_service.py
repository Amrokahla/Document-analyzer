from PIL import Image
import pytesseract
import io

def perform_ocr(file_bytes: bytes) -> str:
    """Run OCR on image bytes and return extracted text."""
    try:
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"OCR failed: {str(e)}"
