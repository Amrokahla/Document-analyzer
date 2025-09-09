import re
import logging
from typing import Dict

logger = logging.getLogger(__name__)

def extract_invoice_fields(text: str) -> Dict[str, str]:
    logger.info("Extracting fields for document type: invoice")
    fields = {}
    try:
        match = re.search(r"(Invoice\s*Number[:\s]*\w+)", text, re.IGNORECASE)
        if match:
            fields["invoice_number"] = match.group(1).split()[-1]

        match = re.search(r"(\$?\d+[.,]?\d*\s?(USD)?)", text)
        if match:
            fields["total"] = match.group(1)

        match = re.search(r"(\d{2}/\d{2}/\d{4})", text)
        if match:
            fields["date"] = match.group(1)

        logger.debug("Extracted invoice fields: %s", fields)
    except Exception as e:
        logger.exception("Invoice field extraction failed: %s", str(e))
    return fields


def extract_email_fields(text: str) -> Dict[str, str]:
    logger.info("Extracting fields for document type: email")
    fields = {}
    try:
        match = re.search(r"From:\s*(.+)", text)
        if match:
            fields["from"] = match.group(1).strip()

        match = re.search(r"To:\s*(.+)", text)
        if match:
            fields["to"] = match.group(1).strip()

        match = re.search(r"Subject:\s*(.+)", text)
        if match:
            fields["subject"] = match.group(1).strip()

        logger.debug("Extracted email fields: %s", fields)
    except Exception as e:
        logger.exception("Email field extraction failed: %s", str(e))
    return fields


def extract_resume_fields(text: str) -> Dict[str, str]:
    logger.info("Extracting fields for document type: resume")
    fields = {}
    try:
        first_line = text.split("\n")[0].strip()
        if len(first_line.split()) >= 2:
            fields["name"] = first_line

        match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        if match:
            fields["email"] = match.group(0)

        match = re.search(r"(\+?\d[\d\s\-]{7,}\d)", text)
        if match:
            fields["phone"] = match.group(1)

        logger.debug("Extracted resume fields: %s", fields)
    except Exception as e:
        logger.exception("Resume field extraction failed: %s", str(e))
    return fields


def extract_fields(document_type: str, text: str) -> Dict[str, str]:
    logger.info("extract_fields called for document type: %s", document_type)
    try:
        if document_type.lower() == "invoice":
            return extract_invoice_fields(text)
        elif document_type.lower() == "email":
            return extract_email_fields(text)
        elif document_type.lower() == "resume":
            return extract_resume_fields(text)
        else:
            logger.warning("No extraction rules defined for document type: %s", document_type)
            return {}
    except Exception as e:
        logger.exception("Extraction failed for type %s: %s", document_type, str(e))
        return {}
