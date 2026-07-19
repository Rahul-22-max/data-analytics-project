from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.model_loader import model


class PredictionService:

    @staticmethod
    def predict(data: PredictionRequest):

        if model is None:
            print("⚠ Using fallback prediction.")

            return PredictionResponse(
                churn_prediction="No",
                probability=0.91
            )

        # Real prediction will be added later
        return PredictionResponse(
            churn_prediction="Yes",
            probability=0.97
        )