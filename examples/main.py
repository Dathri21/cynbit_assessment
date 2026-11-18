from typing import ClassVar
from urllib.parse import urlparse

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, field_validator

app = FastAPI(
    title="Application API — Reference Example",
    description=(
        "Illustrative API showing server-side validation and duplicate "
        "application handling. This is not Cynbit production code."
    ),
    version="1.0.0",
)


class ApplicationRequest(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(min_length=10, max_length=16)
    whatsapp_number: str = Field(min_length=10, max_length=16)
    permanent_address: str = Field(min_length=5, max_length=300)
    resume_or_portfolio_url: str = Field(min_length=8, max_length=500)

    @field_validator(
        "full_name", "phone", "whatsapp_number",
        "permanent_address", "resume_or_portfolio_url"
    )
    @classmethod
    def strip_and_reject_blank(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("This field is required.")
        return cleaned

    @field_validator("resume_or_portfolio_url")
    @classmethod
    def require_http_url(cls, value: str) -> str:
        parsed = urlparse(value)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Enter a valid HTTP or HTTPS URL.")
        return value


class ApplicationResponse(BaseModel):
    message: str
    application_status: str


# Demonstration only. Use a persistent database with a UNIQUE constraint
# and transaction-safe insert in a real production application.
submitted_emails: set[str] = set()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post(
    "/applications",
    response_model=ApplicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_application(payload: ApplicationRequest):
    normalized_email = str(payload.email).strip().lower()

    if normalized_email in submitted_emails:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "code": "DUPLICATE_APPLICATION",
                "message": "An application already exists for this email address.",
            },
        )

    submitted_emails.add(normalized_email)

    return ApplicationResponse(
        message="Application received successfully.",
        application_status="submitted",
    )
