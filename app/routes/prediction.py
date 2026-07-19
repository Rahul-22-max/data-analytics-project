from fastapi import APIRouter
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.utils.logger import logger

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post("/", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    logger.info("Prediction API called")

    logger.info(f"Request Data: {request}")

    return PredictionResponse(
        churn_prediction="No",
        probability=0.93
    )