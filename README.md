# Cynbit Backend Technical Audit — Assessment Submission

This repository contains a backend-focused audit report and a small FastAPI reference implementation prepared for the Cynbit Backend Developer Intern assessment.

## Contents

- `BACKEND_AUDIT_REPORT.md` — full audit report, evidence, limitations, findings, recommendations, and a dedicated Browser Network Tab Analysis section.
- `NETWORK_TAB_CHECKLIST.md` — practical checklist for inspecting requests, responses, status codes, timings, and safely capturing evidence.
- `examples/main.py` — illustrative FastAPI form endpoint with validation and duplicate handling.
- `requirements.txt` — Python dependencies.
- `tests/test_main.py` — basic API tests.
- `.gitignore` — excludes local environments and secrets.

## Run locally

Python 3.10+ is recommended.

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```powershell
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn examples.main:app --reload
```

Open the interactive API documentation at:

`http://127.0.0.1:8000/docs`

Run tests:

```bash
pytest -q
```

## Important assessment note

The FastAPI implementation is a proposed example demonstrating recommended backend practices. It is not Cynbit's source code and does not claim to reproduce Cynbit's production architecture.

The report is based on public website content and applicant-reported manual observations. Actual API endpoints, payloads, database schema, response headers, server-side validation, and internal security controls were not inspected. The Network Tab section therefore records these as pending verification rather than inventing failures or status codes. See the report's scope and limitations before interpreting findings.

## Suggested Git commands

```bash
git init
git add .
git commit -m "Add Cynbit backend audit and FastAPI examples"
```

Create a public GitHub repository, then connect it using the repository URL shown by GitHub:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/cynbit-backend-technical-audit.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. Do not commit real applicant information, passwords, API keys, or private screenshots.
