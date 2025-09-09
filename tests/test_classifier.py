from backend.services.classifier_service import predict_document_type

def test_classifier_with_invoice_text():
    text = "Invoice Number: 12345\nTotal: $500\nDate: 01/01/2023"
    prediction = predict_document_type(text)
    assert prediction in ["invoice", "unknown"]

def test_classifier_with_email_text():
    text = "From: alice@example.com\nTo: bob@example.com\nSubject: Meeting"
    prediction = predict_document_type(text)
    assert prediction in ["email", "unknown"]
