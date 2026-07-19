from fastapi import APIRouter

from app.core.config import settings
from app.schemas.response import APIResponse
from app.services.model_loader import model

router = APIRouter(
    tags=["ℹ️ Info"]
)


@router.get(
    "/info",
    response_model=APIResponse,
    summary="API Information",
    description="Returns application information."
)
def get_info():

    return APIResponse(
        success=True,
        message="API Information",
        data={
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": "Development",
            "model_loaded": model is not None
        }
    )