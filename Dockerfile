# 1. Base image (lightweight Python with build tools)
FROM python:3.12

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies (needed for OCR & Poetry)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# 4. Install Poetry
ENV POETRY_HOME="/opt/poetry"
RUN pip install poetry

# 5. Copy project files
COPY pyproject.toml poetry.lock ./
COPY backend ./backend
COPY main.py ./
COPY frontend ./frontend

# 6. Install dependencies with Poetry
RUN poetry install --no-root

# 7. Expose app port
EXPOSE 8000

# 8. Run FastAPI with Uvicorn
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
