from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "status": "success",
        "message": "Customer Churn & LTV Prediction API is running!",
        "version": "1.0.0"
    }