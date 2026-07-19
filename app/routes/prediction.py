from fastapi import APIRouter, Depends

from app.schemas.prediction import (
    PredictionRequest,
)
from app.schemas.response import APIResponse
from app.services.prediction_service import PredictionService
from app.dependencies.prediction_dependency import (
    get_prediction_service,
)
from app.utils.logger import logger

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

router = APIRouter(
    prefix="/predict",
    tags=["🤖 Prediction"]
)


@router.post(
    "/",
    response_model=APIResponse,
    summary="Predict Customer Churn",
    description="""
Predict whether a customer is likely to churn based on:

- Customer tenure
- Monthly charges
- Contract type
""",
    response_description="Standard API Response"
)
def predict(
    request: PredictionRequest,
    service: PredictionService = Depends(get_prediction_service)
):

    logger.info("Prediction API called")
    logger.info(f"Request Data: {request}")

    prediction = service.predict(request)

    logger.info(f"Prediction Response: {prediction}")

    return APIResponse(
        success=True,
        message="Prediction successful",
        data=prediction
    )