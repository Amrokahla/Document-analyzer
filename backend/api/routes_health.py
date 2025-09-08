from fastapi import APIRouter
from backend.api.schemas import HealthResponse
from backend.services.health_service import check_liveness, check_readiness

router = APIRouter()

@router.get("/health/live", response_model=HealthResponse)
async def health_live():
    return check_liveness()

@router.get("/health/ready", response_model=HealthResponse)
async def health_ready():
    return check_readiness()
