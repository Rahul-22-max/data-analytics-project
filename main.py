from fastapi import FastAPI
from app.routes.home import router as home_router

app = FastAPI(
    title="Customer Churn & LTV Prediction API",
    description="Backend API for Customer Churn Prediction and Lifetime Value Estimation",
    version="1.0.0"
)

app.include_router(home_router)