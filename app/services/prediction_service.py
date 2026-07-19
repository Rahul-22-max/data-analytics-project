from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.model_loader import model
from app.services.preprocessing import preprocess_input


class PredictionService:

    @staticmethod
    def predict(data: PredictionRequest):

        features = preprocess_input(data)

        print(features)

        if model is None:
            print("⚠ Using fallback prediction.")

            return PredictionResponse(
                churn_prediction="No",
                probability=0.91
            )

        # This will be used when the real model is added
        prediction = model.predict(features)[0]

        probability = model.predict_proba(features)[0][1]

        return PredictionResponse(
            churn_prediction="Yes" if prediction == 1 else "No",
            probability=round(float(probability), 2)
        )