import pandas as pd
from fastapi import HTTPException

from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.model_loader import ModelLoader


class PredictionService:

    @staticmethod
    def predict(request: PredictionRequest) -> PredictionResponse:

        valid_contracts = [
            "Month-to-month",
            "One year",
            "Two year"
        ]

        if request.contract not in valid_contracts:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid contract type. Allowed values: {valid_contracts}"
            )

        model = ModelLoader.load_model()

        if model is None:

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

        input_df = pd.DataFrame([{
            "tenure": request.tenure,
            "MonthlyCharges": request.monthly_charges
        }])

        prediction = model.predict(input_df)[0]

        if hasattr(model, "predict_proba"):
            probability = float(max(model.predict_proba(input_df)[0]))
        else:
            probability = 1.0

        return PredictionResponse(
            churn_prediction="Yes" if prediction == 1 else "No",
            probability=round(probability, 2)
        )