from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.model_loader import model
from app.services.preprocessing import preprocess_input
from app.core.exceptions import APIException


class PredictionService:

    @staticmethod
    def predict(data: PredictionRequest):

        # Business validations
        if data.tenure < 0:
            raise APIException(
                message="Tenure cannot be negative.",
                status_code=400
            )

        if data.monthly_charges < 0:
            raise APIException(
                message="Monthly charges cannot be negative.",
                status_code=400
            )

        # Convert request into DataFrame
        features = preprocess_input(data)

        print(features)

        # Fallback prediction if model is unavailable
        if model is None:
            print("⚠ Using fallback prediction.")

            response = PredictionResponse(
                churn_prediction="No",
                probability=0.91
            )

            return response

        # Real prediction (when model is available)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        response = PredictionResponse(
            churn_prediction="Yes" if prediction == 1 else "No",
            probability=round(float(probability), 2)
        )

        return response