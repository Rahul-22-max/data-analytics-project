from app.schemas.prediction import PredictionRequest, PredictionResponse


class PredictionService:

    @staticmethod
    def predict(request: PredictionRequest) -> PredictionResponse:

        if request.tenure < 12:
            prediction = "Yes"
            probability = 0.82
        else:
            prediction = "No"
            probability = 0.91

        return PredictionResponse(
            churn_prediction=prediction,
            probability=probability
        )