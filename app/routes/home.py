from fastapi import APIRouter
from app.schemas.response import APIResponse

router = APIRouter(tags=["Home"])


@router.get("/", response_model=APIResponse)
def home():

    return APIResponse(
        success=True,
        message="API is running",
        data={
            "project": "Customer Churn Prediction API"
        }
    )