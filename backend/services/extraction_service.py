import re
from typing import Dict


def extract_invoice_fields(text: str) -> Dict[str, str]:
    """Extract basic invoice fields using regex."""
    fields = {}
    # Invoice number
    match = re.search(r"(Invoice\s*Number[:\s]*\w+)", text, re.IGNORECASE)
    if match:
        fields["invoice_number"] = match.group(1).split()[-1]
    # Total amount (looking for patterns like $123.45)
    match = re.search(r"(\$?\d+[.,]?\d*\s?(USD)?)", text)
    if match:
        fields["total"] = match.group(1)
    # Date
    match = re.search(r"(\d{2}/\d{2}/\d{4})", text)
    if match:
        fields["date"] = match.group(1)
    return fields


def extract_email_fields(text: str) -> Dict[str, str]:
    """Extract basic email fields."""
    fields = {}
    # From
    match = re.search(r"From:\s*(.+)", text)
    if match:
        fields["from"] = match.group(1).strip()
    # To
    match = re.search(r"To:\s*(.+)", text)
    if match:
        fields["to"] = match.group(1).strip()
    # Subject
    match = re.search(r"Subject:\s*(.+)", text)
    if match:
        fields["subject"] = match.group(1).strip()
    return fields


def extract_resume_fields(text: str) -> Dict[str, str]:
    """Extract basic resume fields."""
    fields = {}
    # Name (assume first line is name)
    first_line = text.split("\n")[0].strip()
    if len(first_line.split()) >= 2:
        fields["name"] = first_line
    # Email
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    if match:
        fields["email"] = match.group(0)
    # Phone
    match = re.search(r"(\+?\d[\d\s\-]{7,}\d)", text)
    if match:
        fields["phone"] = match.group(1)
    return fields


def extract_fields(document_type: str, text: str) -> Dict[str, str]:
    """Dispatch extraction logic based on doc type."""
    if document_type.lower() == "invoice":
        return extract_invoice_fields(text)
    elif document_type.lower() == "email":
        return extract_email_fields(text)
    elif document_type.lower() == "resume":
        return extract_resume_fields(text)
    return {}
