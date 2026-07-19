from pydantic import BaseModel


class PredictionRequest(BaseModel):
    tenure: int
    monthly_charges: float
    contract: str


class PredictionResponse(BaseModel):
    churn_prediction: str
    probability: float