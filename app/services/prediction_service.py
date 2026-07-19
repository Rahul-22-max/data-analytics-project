from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.model_loader import ModelLoader


class PredictionService:

    @staticmethod
    def predict(request: PredictionRequest) -> PredictionResponse:

        model = ModelLoader.load_model()

        # Real model will be used later
        if model is None:

            if request.tenure < 12:
                prediction = "Yes"
                probability = 0.82
            else:
                prediction = "No"
                probability = 0.91

        else:
            # Placeholder until we integrate the trained model
            prediction = "No"
            probability = 0.95

        return PredictionResponse(
            churn_prediction=prediction,
            probability=probability
        )