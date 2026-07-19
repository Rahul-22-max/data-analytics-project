from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.services.model_loader import model


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("=" * 50)
    print("Customer Churn Prediction API Started")

    if model is None:
        print("⚠ ML Model not loaded")
    else:
        print("✅ ML Model loaded successfully")

    print("=" * 50)

    yield

    print("=" * 50)
    print("Customer Churn Prediction API Stopped")
    print("=" * 50)