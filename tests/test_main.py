from fastapi.testclient import TestClient
from examples.main import app, submitted_emails

client = TestClient(app)


def setup_function():
    submitted_emails.clear()


def valid_payload():
    return {
        "full_name": "Amara Example",
        "email": "amara@example.com",
        "phone": "9876543210",
        "whatsapp_number": "9876543210",
        "permanent_address": "Example address, India",
        "resume_or_portfolio_url": "https://example.com/resume",
    }


def test_application_created():
    response = client.post("/applications", json=valid_payload())
    assert response.status_code == 201
    assert response.json()["application_status"] == "submitted"


def test_invalid_email_is_rejected():
    payload = valid_payload()
    payload["email"] = "not-an-email"
    response = client.post("/applications", json=payload)
    assert response.status_code == 422


def test_invalid_resume_url_is_rejected():
    payload = valid_payload()
    payload["resume_or_portfolio_url"] = "abcd123"
    response = client.post("/applications", json=payload)
    assert response.status_code == 422


def test_name_length_is_bounded():
    payload = valid_payload()
    payload["full_name"] = "A" * 101
    response = client.post("/applications", json=payload)
    assert response.status_code == 422


def test_duplicate_email_returns_conflict():
    payload = valid_payload()
    first = client.post("/applications", json=payload)
    second = client.post("/applications", json=payload)
    assert first.status_code == 201
    assert second.status_code == 409
