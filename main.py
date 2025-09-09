import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.api import routes_ocr, routes_health
from backend.core.error_handlers import add_exception_handlers
from backend.core.logging_config import configure_logging


configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Document AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_exception_handlers(app)

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Application startup: Document AI API is launching")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 Application shutdown: Document AI API is stopping")

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info("➡️  Request start: %s %s", request.method, request.url.path)
    try:
        response = await call_next(request)
        logger.info("⬅️  Request end: %s %s -> %s", request.method, request.url.path, response.status_code)
        return response
    except Exception as e:
        logger.exception("❌ Exception during request %s %s: %s", request.method, request.url.path, str(e))
        raise

# Routers
app.include_router(routes_ocr.router, prefix="/api", tags=["Document Analyzing"])
app.include_router(routes_health.router, prefix="/api", tags=["Health Check"])
