# Cynbit Technologies — Backend-Focused Website Audit

**Prepared for:** Backend Developer Intern  
**Applicant:** Amara Dathri Lakshmi Anuhya  
**Website:** https://www.cynbit.in  
  
**Scope:** Passive review of publicly accessible website pages and applicant-reported form interactions

---

## 1. Executive summary

This report reviews Cynbit's publicly accessible website from a backend developer's perspective. The review focuses on the Careers application experience, the Contact form, privacy-policy transparency, and publicly stated technology/service information.

The review identified the following improvement opportunities:

1. **Form validation feedback is delayed until submission.** During the applicant's manual testing of the Careers form, invalid or missing values were reported after clicking Submit rather than being explained inline as the applicant completed each field.
2. **The Full Name field appeared to accept a long value (approximately 100–150 characters) without an immediate length warning or restriction.** This is a data-quality and validation improvement opportunity, not evidence of a security vulnerability. The exact accepted maximum was not measured.
3. **The privacy policy does not state a clear retention period for applicant data.** A retention schedule would make the lifecycle of application data more transparent.

The review also recorded positive behaviour: the applicant reported that duplicate applications using the same email were identified immediately with an error message; the Contact form submitted successfully; site navigation and page rendering worked normally; and Chrome reported the HTTPS connection as secure.

**Important scope limitation:** This was not a source-code review or a complete API/security test. The applicant did not have access to desktop browser developer tools during the review. Therefore, API endpoints, HTTP methods, request/response payloads, database schema, authentication implementation, server-side validation, encryption-at-rest configuration, and production performance metrics were not independently inspected. No claim in this report should be read as confirmation that an unobserved control is absent.

---

## 2. Scope and methodology

### 2.1 Public pages considered

- Homepage: https://www.cynbit.in/
- Careers: https://www.cynbit.in/careers
- Contact: https://www.cynbit.in/contact
- Privacy policy: the policy text supplied during the assessment and the publicly indexed policy page at https://cynbitwebsite.vercel.app/privacy

### 2.2 Method

The review used normal browser interaction and passive observation only:
- Opened publicly accessible pages.
- Reviewed the Contact and Careers form experience.
- Entered test values into form fields without attempting to bypass controls or access restricted data.
- Observed validation feedback and duplicate-application messaging as reported by the applicant.
- Reviewed the privacy-policy text.
- Checked that the browser reported the website connection as secure.
- Observed navigation, image loading, scrolling, and general page responsiveness.

No vulnerability scanning, brute force, automated traffic, endpoint fuzzing, unauthorized access, or disruptive testing was performed.

### 2.3 Evidence classification

Each observation is labelled as one of:
- **Observed/reported:** directly seen during the applicant's manual browser review.
- **Publicly stated:** described by Cynbit's public website or policy.
- **Not verified:** requires browser developer tools, source code, server access, or confirmation from Cynbit.

---

## 3. Publicly observable architecture and data flow

### 3.1 What can be established

Cynbit's public website describes services in software development, AI automation, SaaS products, and cloud systems. Its Careers page lists a Backend Developer Intern role and describes the company's remote/Jaipur operating model.

The published privacy-policy text identifies:
- Resend as an email-delivery service.
- Prisma as a database-management technology.
- Inquiry forms and BitElevate applications as sources of submitted information.
- Applicant/contact information such as name, email, and professional context.

These are public statements. They do not independently prove the exact production architecture or establish which service handles each individual form.

### 3.2 Plausible high-level form flow (inferred, not verified)

A conventional implementation for a website form of this type could follow this flow:

1. Browser collects form values.
2. Frontend performs immediate usability validation.
3. Browser sends a request to a server endpoint over HTTPS.
4. Server validates and normalizes the submitted data.
5. Server applies duplicate-submission rules.
6. Server persists the application record through a database layer.
7. Server may trigger an email notification through an email provider.
8. Server returns a structured success or validation response.
9. Frontend displays a confirmation or field-specific errors.

This is a recommended reference flow, not a description of Cynbit's confirmed internal implementation.

### 3.3 API inventory

| Area | Public behaviour reviewed | API details |
|---|---|---|
| Contact form | Applicant reported successful submission | Endpoint, method and payload not inspected |
| Careers application | Submission-time validation messages observed/reported | Endpoint, method and payload not inspected |
| Duplicate application | Same-email attempt reportedly produced an immediate already-applied message | Backend enforcement mechanism not inspected |
| Page navigation | Pages and links worked during manual review | Not an API finding |

The assessment should not invent endpoint paths, HTTP methods, payload fields, response codes, or authentication mechanisms. These should be added only after inspection in browser Developer Tools.

---

## 4. Findings and recommendations

### Finding 01 — Submission-only validation feedback

**Category:** Input validation / usability  
**Priority:** Medium  
**Evidence:** During manual Careers-form testing, invalid or missing values (including email, phone, WhatsApp number, permanent address, and resume/portfolio URL) were reported after the user clicked Submit. The form then focused or navigated to the relevant field and displayed validation feedback.  
**Impact:** Users may complete most of a long form before learning that one or more values are invalid. This increases correction effort and can lead to repeated submission attempts.  
**Recommendation:**
- Validate fields on blur and, where helpful, while typing.
- Show a clear error beside the affected field.
- Preserve entered values after validation errors.
- Show an error summary at the top for long forms and move focus to the first invalid field.
- Keep server-side validation authoritative; frontend validation is not a security boundary.
**Verification status:** Applicant-reported manual observation. Actual API response format and server-side validation were not inspected.

### Finding 02 — Full Name input length should be explicitly bounded

**Category:** Data validation / data quality  
**Priority:** Low  
**Evidence:** Applicant reported that the Full Name field accepted a test value of approximately 100–150 characters without an immediate length warning or restriction. The exact maximum accepted length and server-side behaviour were not measured.  
**Impact:** Unbounded or excessively large values can create inconsistent records, increase storage/processing unnecessarily, and complicate downstream display and data quality. A 100–150 character value alone is not proof of a vulnerability.  
**Recommendation:**
- Define a reasonable maximum based on product requirements.
- Enforce the same limit in the frontend, API schema, and database column.
- Trim leading/trailing whitespace and reject blank-after-trim values.
- Return a field-specific validation error.
**Verification status:** Applicant-reported; exact maximum and backend enforcement not verified.

### Finding 03 — Privacy policy should state applicant-data retention

**Category:** Privacy / data lifecycle transparency  
**Priority:** Medium  
**Evidence:** The privacy-policy text reviewed during the assessment describes collection, use, security, and third-party services, but no clear retention period was present in the supplied text or publicly indexed policy content reviewed.  
**Impact:** Applicants cannot easily understand how long application data may be kept or what event triggers deletion.  
**Recommendation:**
- Publish retention periods or clear retention criteria for unsuccessful applications, successful hires, inquiries, and operational logs.
- Explain exceptions such as legal obligations or dispute handling.
- Describe secure deletion and backup-expiry practices at a suitable level.
- Ensure the published policy matches actual operational retention settings.
**Verification status:** Policy-text observation; internal retention configuration was not inspected.

### Finding 04 — Clarify the process for correcting applicant data

**Category:** Privacy / user rights transparency  
**Priority:** Low  
**Evidence:** The excerpt supplied by the applicant contained sections 1–4 and did not include a correction procedure. The publicly indexed policy page contains a Section 5 stating that individuals may request a copy of their data or permanent deletion by contacting opportunities@cynbit.in, but it does not clearly describe a correction/update workflow in the indexed text.  
**Impact:** Applicants may not know how to correct an inaccurate phone number, email, or other application detail after submission.  
**Recommendation:**
- Add a clear correction/update request process and contact channel.
- Explain what information an applicant should provide to locate their record safely.
- Verify the requester before disclosing or changing personal information.
- Document request handling and completion.
**Verification status:** Public policy wording reviewed; no internal request workflow tested. Note that the live/indexed policy includes copy and deletion rights, so this report does not claim those rights are entirely absent.

---

## 5. Positive observations

These are useful controls or behaviours observed during the manual review. They are not a substitute for technical verification.

| Area | Observation | Limitation |
|---|---|---|
| Duplicate applications | Applicant reported that reusing the same email immediately displayed an already-applied message | Database uniqueness constraint and race-condition handling not verified |
| Contact form | Applicant reported successful submission | API response and persistence not inspected |
| HTTPS | Chrome displayed “Connection is secure” | Does not prove secure headers, TLS configuration quality, or encryption at rest |
| Navigation | Applicant reported navigation links opened correctly | Not a comprehensive link crawler |
| Rendering/performance | Applicant reported images, scrolling, and pages worked smoothly | No timing, load, or stress measurements performed |

---

## 6. Recommended backend design

The following is a proposed reference design for a form API. It is not a reverse-engineered representation of Cynbit's production system.

### 6.1 Request validation

Use a schema to validate input on the server:
- Required fields must not be blank after trimming.
- Email must use a valid email format.
- Phone fields should be normalized and validated according to the accepted country/format rules.
- Resume/portfolio URL should be parsed as an HTTP or HTTPS URL.
- Text fields should have explicit maximum lengths.
- Reject unexpected or oversized request bodies.

### 6.2 Consistent error responses

Return a structured response with a stable error code and field-level details. The frontend can map these errors to the correct fields.

Example:

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "Enter a valid email address.",
      "type": "value_error"
    }
  ]
}
```

Do not expose stack traces, database details, secrets, or internal implementation information to the browser.

### 6.3 Duplicate application handling

A robust implementation should:
- Normalize email addresses consistently.
- Enforce uniqueness in the database for the relevant application scope.
- Catch database uniqueness conflicts and return a clear conflict response (HTTP 409).
- Avoid relying only on a frontend check, because two requests can arrive at nearly the same time.

Whether Cynbit uses this design is not known from public observation.

### 6.4 Privacy and security controls

Recommended controls include:
- HTTPS for all pages and form submissions.
- Server-side validation independent of browser validation.
- Least-privilege access to applicant records.
- Secrets stored in environment variables or a secrets manager, never in frontend code or Git.
- Avoid logging full resumes, phone numbers, addresses, or other unnecessary personal data.
- Define retention and deletion workflows, including backup lifecycle.
- Apply request-size limits and reasonable rate limiting to public form endpoints.
- Use generic server errors and detailed internal logs with appropriate access controls.
- Verify identity before fulfilling access, correction, or deletion requests.

---

## 7. Example code

The `examples/` folder contains a small FastAPI reference implementation demonstrating:
- Pydantic field validation and length bounds.
- Email and URL validation.
- A structured application endpoint.
- Duplicate email detection in an in-memory demonstration store.
- HTTP 409 for duplicate applications.
- Field-specific validation responses through FastAPI.

**Important:** The example uses an in-memory set for demonstration only. It is not production persistence, does not establish Cynbit's implementation, and must be replaced with a database transaction and unique constraint in a production system.

---

## 8. Browser Network Tab Analysis and Further Verification

### 8.1 Evidence status

**Status: Not independently verified — no Network-tab defect is claimed in this report.** The applicant's earlier review was performed through normal page interaction, without desktop browser Developer Tools. Therefore, this assessment does not have a saved HAR file, request/response trace, endpoint list, or measured request timings. It would be inaccurate to report specific failed requests, HTTP status codes, slow APIs, duplicate calls, or payload defects as observed findings.

The applicant-reported form behaviour remains limited to the visible UI: a validation message appears after submission for an invalid email, the form displays an error for a duplicate email, and navigation works. These UI observations do not establish the underlying HTTP status code or prove how the server validates the data.

### 8.2 Network checks to perform

Use Chrome on a desktop/laptop and inspect the Careers and Contact flows with DevTools open. The Network panel records requests while it is open. Review the following:

| Area | What to inspect | What would warrant a finding |
|---|---|---|
| Request status | Status column for document, script, image, and Fetch/XHR requests | Unexpected 4xx/5xx, CORS errors, or failed resources during a normal user flow |
| Form submission | Fetch/XHR request triggered by Submit; URL path and HTTP method | Request not sent, wrong method/path, or unexpected repeated submission |
| Payload | Payload tab; record field names and data types only | Missing, malformed, or unnecessary fields; never copy real applicant values into the report |
| Response | Response/Preview tab and status code for valid and invalid test submissions | UI and server response disagree, unclear error response, or sensitive data returned unnecessarily |
| Timing | Time column and Timing tab | Reproducibly slow request under ordinary conditions; record actual duration and test conditions |
| Duplicate requests | Compare requests triggered by a single click | Multiple equivalent submissions from one deliberate action, after ruling out retries/preflight requests |
| Headers/cookies | Headers tab, including security-related response headers and cookie attributes | Missing or weak configuration that is actually visible in the captured response; interpret in context |
| Resources | Failed CSS, JavaScript, image, font, or document requests | Broken resource that affects page rendering or functionality |

### 8.3 Current finding register

- **Confirmed Network-tab failures:** None established from the evidence available for this assessment.
- **HTTP status codes and response payloads:** Not captured; verification pending.
- **API response-time measurements:** Not captured; verification pending.
- **Duplicate network submissions:** Not tested; verification pending.
- **Request/response security headers and cookie attributes:** Not captured; verification pending.

These are evidence gaps, not confirmed defects. Do not convert them into negative findings without a corresponding trace or screenshot. A browser's displayed form error alone is not enough to infer an HTTP status code.

### 8.4 Safe evidence collection procedure

1. Open the Careers page in desktop Chrome and press `F12` (or `Ctrl+Shift+I`), then select **Network**.
2. Enable **Preserve log**, clear the request list, and reload the page.
3. Filter to **Fetch/XHR**, then submit only synthetic test values where the form permits it. Do not submit another person's information or repeatedly create real applications.
4. Inspect the request's **Headers**, **Payload**, **Response**, and **Timing** tabs. Record the method, path, status, duration, and field names; redact email addresses, names, tokens, cookies, and other personal data.
5. Repeat only the normal valid/invalid UI flows needed to understand the behaviour. Do not fuzz endpoints, replay sensitive requests, test concurrency, or run load/security scans against production without explicit authorization.
6. Capture a screenshot of the Network request list and relevant request details only after redacting personal data and secrets. A sanitized HAR export may be useful, but HAR files can contain credentials, cookies, tokens, and form data; do not submit an unredacted HAR.

### 8.5 Additional developer-tool checks

The following remain open for authorized verification: server-side validation, response headers and cookie attributes, request-size limits, rate limiting, sensitive-value logging, concurrency-safe duplicate handling, and database retention/deletion procedures. Prefer a staging environment with test accounts and synthetic data for deeper testing.

---

## 9. Conclusion

The public website and applicant-facing forms showed several positive behaviours during manual review, including working navigation, successful Contact form submission, browser-reported HTTPS security, and immediate duplicate-application messaging. The most actionable improvement is to provide clearer field-level validation before final submission while retaining server-side validation.

The privacy policy would also benefit from explicit retention criteria and a clearer correction-request process. Input length limits should be defined consistently across the browser, API, and database.

This report intentionally distinguishes direct observations from recommendations and unverified implementation details. A complete API and architecture audit would require authorized access to browser network traces, technical documentation, or a staging environment.
