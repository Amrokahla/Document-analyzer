from fastapi import APIRouter, UploadFile, File
from backend.api.schemas import DocumentResponse

router = APIRouter()

@router.post("/process-document", response_model=DocumentResponse)
async def process_document(file: UploadFile = File(...)):
    
    # For now: return mock response until OCR & classifier are ready
    return DocumentResponse(
        filename=file.filename,
        document_type="invoice",
        extracted_data={"total": "$250", "date": "2024-01-01"},
        extracted_text="This is example OCR text."
    )
