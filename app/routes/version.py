from fastapi import APIRouter

from app.core.config import settings
from app.schemas.response import APIResponse

router = APIRouter(
    tags=["🏷️ Version"]
)


@router.get(
    "/version",
    response_model=APIResponse,
    summary="API Version",
    description="Returns API version information."
)
def get_version():

    return APIResponse(
        success=True,
        message="API Version",
        data={
            "name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "api_prefix": settings.API_PREFIX
        }
    )