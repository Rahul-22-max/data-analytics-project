import pandas as pd

from fastapi import APIRouter

from .schemas import CustomerData

from .predictor import predict

router = APIRouter()

@router.post("/predict")

def predict_ltv(customer: CustomerData):

    df = pd.DataFrame([customer.dict()])

    result = predict(df)

    return {
        "Predicted_LTV": result
    }