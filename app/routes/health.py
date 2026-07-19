from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():
    return {
        "status": "Healthy",
        "service": "Customer Churn Prediction API",
        "version": "1.0.0"
    }