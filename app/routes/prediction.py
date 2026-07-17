from fastapi import APIRouter
from app.schemas.prediction import PredictionRequest, PredictionResponse

router = APIRouter(prefix="/predict", tags=["Prediction"])


@router.post("/", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    return PredictionResponse(
        churn_prediction="No",
        probability=0.93
    )