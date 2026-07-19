from fastapi import APIRouter
from app.schemas.response import APIResponse

router = APIRouter(
    tags=["❤️ Health"]
)


@router.get(
    "/health",
    response_model=APIResponse,
    summary="Health Check",
    description="Checks if the API is healthy."
)
def health():

    return APIResponse(
        success=True,
        message="Health check successful",
        data={
            "status": "healthy"
        }
    )