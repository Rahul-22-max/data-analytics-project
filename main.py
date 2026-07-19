from fastapi import FastAPI

from app.core.config import settings
from app.core.exceptions import global_exception_handler

from app.routes.home import router as home_router
from app.routes.prediction import router as prediction_router
from app.routes.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    description="""
Customer Churn Prediction API

Features:
- Predict customer churn
- Health check endpoint
- Logging
- Input validation
- Exception handling
""",
    version=settings.APP_VERSION,
    contact={
        "name": "Rahul Charan",
        "email": "rahul@example.com"
    },
)

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(home_router)
app.include_router(prediction_router)
app.include_router(health_router)