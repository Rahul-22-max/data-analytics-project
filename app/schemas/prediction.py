from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    tenure: int = Field(
        ...,
        example=12,
        description="Customer tenure in months"
    )

    monthly_charges: float = Field(
        ...,
        example=75.50,
        description="Monthly bill amount"
    )

    contract: str = Field(
        ...,
        example="Month-to-month",
        description="Contract type"
    )


class PredictionResponse(BaseModel):
    churn_prediction: str = Field(
        ...,
        example="No"
    )

    probability: float = Field(
        ...,
        example=0.91
    )