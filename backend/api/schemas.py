from pydantic import BaseModel
from typing import Dict, Optional

class DocumentResponse(BaseModel):
    filename: str
    document_type: str
    extracted_data: Dict[str, str] = {}
    extracted_text: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    model_path: Optional[str] = None
    vectorizer_path: Optional[str] = None
    model_files_present: Optional[bool] = None