import pandas as pd

from fastapi import APIRouter

from .schemas import CustomerData

from .predictor import predict_ltv

router = APIRouter()

@router.post("/predict")
def predict(customer: CustomerData):

    result = predict_ltv(customer.model_dump())

    return result