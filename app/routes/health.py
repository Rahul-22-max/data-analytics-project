from fastapi import APIRouter
from app.schemas.response import APIResponse

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=APIResponse)
def health():

    return APIResponse(
        success=True,
        message="Health check successful",
        data={
            "status": "healthy"
        }
    )