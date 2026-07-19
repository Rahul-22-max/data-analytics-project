from fastapi import APIRouter, Depends

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)
from app.services.prediction_service import PredictionService
from app.dependencies.prediction_dependency import (
    get_prediction_service,
)
from app.utils.logger import logger

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post(
    "/",
    response_model=PredictionResponse,
    summary="Predict Customer Churn",
    description="""
Predict whether a customer is likely to churn based on:

- Customer tenure
- Monthly charges
- Contract type
""",
    response_description="Prediction result with probability"
)
def predict(
    request: PredictionRequest,
    service: PredictionService = Depends(get_prediction_service)
):
    logger.info("Prediction API called")
    logger.info(f"Request Data: {request}")

    response = service.predict(request)

    logger.info(f"Prediction Response: {response}")

    return response