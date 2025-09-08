from fastapi import APIRouter, UploadFile, File
from backend.api.schemas import DocumentResponse
from backend.services.ocr_service import perform_ocr
from backend.services.classifier_service import predict_document_type
from backend.services.extraction_service import extract_fields


router = APIRouter()

@router.post("/process-document", response_model=DocumentResponse)
async def process_document(file: UploadFile = File(...)):
    file_bytes = await file.read()

    # OCR
    extracted_text = perform_ocr(file_bytes)

    # Classification
    doc_type = predict_document_type(extracted_text)

    # Extracted data
    extracted_data = extract_fields(doc_type, extracted_text)


    return DocumentResponse(
        filename=file.filename,
        document_type=doc_type,
        extracted_data=extracted_data,
        extracted_text=extracted_text
    )
