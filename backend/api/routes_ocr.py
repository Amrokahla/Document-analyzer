from fastapi import APIRouter, UploadFile, File
from backend.api.schemas import DocumentResponse
from backend.services.ocr_service import perform_ocr

router = APIRouter()

@router.post("/process-document", response_model=DocumentResponse)
async def process_document(file: UploadFile = File(...)):
    file_bytes = await file.read()
    extracted_text = perform_ocr(file_bytes)

    # For now: OCR only (classifier will be added later)
    return DocumentResponse(
        filename=file.filename,
        document_type="unknown",   # placeholder
        extracted_data={},         # placeholder
        extracted_text=extracted_text
    )
