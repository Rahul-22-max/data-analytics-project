from fastapi import APIRouter

from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction_service import PredictionService
from app.utils.logger import logger

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post("/", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    logger.info("Prediction API called")
    logger.info(f"Request Data: {request}")

    response = PredictionService.predict(request)

    logger.info(f"Prediction Response: {response}")

    return response