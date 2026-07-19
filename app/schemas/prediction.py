from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    tenure: int = Field(..., ge=0, le=100)
    monthly_charges: float = Field(..., ge=0)
    contract: str


class PredictionResponse(BaseModel):
    churn_prediction: str
    probability: float