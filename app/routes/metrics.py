from fastapi import APIRouter

from app.core.config import settings
from app.schemas.response import APIResponse
from app.services.model_loader import model

router = APIRouter(
    tags=["📊 Metrics"]
)


@router.get(
    "/metrics",
    response_model=APIResponse,
    summary="Application Metrics",
    description="Returns application metrics and current status."
)
def get_metrics():

    return APIResponse(
        success=True,
        message="Application Metrics",
        data={
            "api_status": "Healthy",
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": "Development",
            "model_loaded": model is not None,
            "uptime": "Running"
        }
    )