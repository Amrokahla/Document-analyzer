import logging
from fastapi import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

def add_exception_handlers(app):
    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        logger.warning("ValueError at %s: %s", request.url.path, str(exc))
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid input", "detail": str(exc)},
        )

    @app.exception_handler(RuntimeError)
    async def runtime_error_handler(request: Request, exc: RuntimeError):
        logger.error("RuntimeError at %s: %s", request.url.path, str(exc))
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error", "detail": str(exc)},
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception at %s", request.url.path)
        return JSONResponse(
            status_code=500,
            content={"error": "Unexpected error occurred"},
        )
