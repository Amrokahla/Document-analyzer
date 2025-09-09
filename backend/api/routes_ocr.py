import logging
from fastapi import APIRouter, UploadFile, File
from backend.api.schemas import DocumentResponse
from backend.services.ocr_service import perform_ocr
from backend.services.classifier_service import predict_document_type
from backend.services.extraction_service import extract_fields

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/process-document", response_model=DocumentResponse)
async def process_document(file: UploadFile = File(...)):
    logger.info("process-document called with file: %s (content_type=%s)", file.filename, file.content_type)
    try:
        file_bytes = await file.read()
        logger.debug("Read %d bytes from uploaded file %s", len(file_bytes), file.filename)

        # OCR
        extracted_text = perform_ocr(file_bytes)
        logger.debug("OCR text length: %d", len(extracted_text))

        # Classification
        doc_type = predict_document_type(extracted_text)
        logger.info("Document classified as: %s", doc_type)

        # Field extraction
        extracted_data = extract_fields(doc_type, extracted_text)
        logger.debug("Extracted fields: %s", extracted_data)

        response = DocumentResponse(
            filename=file.filename,
            document_type=doc_type,
            extracted_data=extracted_data,
            extracted_text=extracted_text,
        )

        logger.info("process-document completed successfully for file: %s", file.filename)
        return response

    except Exception as e:
        logger.exception("Error while processing file %s: %s", file.filename, str(e))
        raise
