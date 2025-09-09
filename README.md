# Document Layout Analyzer

A lightweight production-style demo that turns PDFs/images → OCR → document classification → structured JSON.
This repo is built for a two-day workshop ("AI: Lab → Production") and shows how to move from lab notebooks to production systems.

---

## Features

* OCR (Pillow + Tesseract)
* Document classification (TF-IDF + Naive Bayes)
* Regex-based field extraction (invoice, email, resume)
* FastAPI backend with health checks (liveness/readiness)
* Logging to console and file
* Config via `.env`
* Notebook for training workflow
* Docker & docker-compose support
* Unit tests with pytest

---

## Requirements

### System

* Linux (Ubuntu) or Windows 10/11
* Python 3.10+
* Tesseract OCR installed
* Docker (optional)

### Python

* Poetry (dependency manager)

---

## Installation

### Linux / macOS

```bash
# Clone repo
git clone <your-repo-url>
cd <repo>

# Install system deps
sudo apt update
sudo apt install -y tesseract-ocr libtesseract-dev poppler-utils build-essential

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Setup env
cp .env.example .env

# Run app
poetry run uvicorn main:app --reload
```

### Windows (PowerShell)

```powershell
# Clone repo
git clone <your-repo-url>
cd <repo>

# Install Tesseract (download from GitHub releases and add to PATH)

# Install Poetry
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Install dependencies
poetry install

# Copy env
copy .env.example .env

# Run app
poetry run uvicorn main:app --reload
```

---

## Frontend

Frontend files are in `frontend/`. To serve them:

```bash
cd frontend
python -m http.server 5500
```

Open: [http://localhost:5500/index.html](http://localhost:5500/index.html)

*(Avoid opening index.html directly with file:// — this causes CORS issues.)*

---

## Docker

```bash
# Build and run
docker compose up --build
```

Open:

* API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
* Frontend: [http://localhost:8000/frontend/index.html](http://localhost:8000/frontend/index.html)

---

## Configuration

`.env.example` → copy to `.env`:

```ini
LOG_LEVEL=INFO
MODEL_DIR=backend/model
OCR_LANG=eng
```

---

## Training (Notebook)

`notebooks/classification.ipynb` shows how to:

1. Convert TIFF dataset → PNG.
2. OCR images → text dataset.
3. Train TF-IDF + Naive Bayes.
4. Save `trained_model.pkl` + `vectorizer.pkl` in `backend/model/`.

Run:

```bash
poetry run jupyter lab
```

---

## API

* `POST /api/process-document` → upload file, returns JSON with OCR, classification, extracted fields.
* `GET /api/health/live` → app heartbeat.
* `GET /api/health/ready` → model readiness check.

---

## Logging

* Logs go to console and `logs/app.log`.
* Level controlled via `.env` (`LOG_LEVEL=DEBUG` etc).

---

## Tests

Run with:

```bash
poetry run pytest -v
```

---

## Troubleshooting

* **Failed to fetch (frontend)** → serve with `http.server` or mount in FastAPI.
* **OCR not working** → check Tesseract installation (`tesseract --version`).
* **Readiness not ready** → ensure model `.pkl` files exist.
* **Docker build fails** → ensure Poetry v2 flag `--without dev` is used.

---

## Workshop Notes

* **Day 1**: Environment setup, OCR, classifier training, FastAPI basics.
* **Day 2**: Extraction, health checks, logging, Dockerization, wrap-up.
