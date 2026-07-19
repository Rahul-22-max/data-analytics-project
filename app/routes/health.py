from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="Health Check",
    description="Check whether API is running",
    response_description="Health status"
)
def health():
    return {
        "status": "healthy"
    }