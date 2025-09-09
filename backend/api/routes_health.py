import logging
from fastapi import APIRouter
from backend.api.schemas import HealthResponse
from backend.services.health_service import check_liveness, check_readiness

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/health/live", response_model=HealthResponse)
async def health_live():
    logger.debug("Endpoint /health/live called")
    result = check_liveness()
    logger.info("Liveness check returned: %s", result["status"])
    return result


@router.get("/health/ready", response_model=HealthResponse)
async def health_ready():
    logger.debug("Endpoint /health/ready called")
    result = check_readiness()
    logger.info("Readiness check returned: %s", result["status"])
    return result
