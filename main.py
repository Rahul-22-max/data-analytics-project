from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.core.config import settings
from app.core.exceptions import APIException, api_exception_handler
from app.middleware.request_logger import RequestLoggerMiddleware
from app.routes.home import router as home_router
from app.routes.health import router as health_router
from app.routes.prediction import router as prediction_router
from app.services.model_loader import model


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("=" * 50)
    print(f"{settings.APP_NAME} Started")

    if model:
        print("✅ ML Model loaded")
    else:
        print("⚠ ML Model not loaded")

    print("=" * 50)

    yield

    print("Application shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    description="""
## Customer Churn Prediction API

This API predicts customer churn.

### Features

- Customer Churn Prediction
- Health Check
- Logging
- Environment Variables
- CORS
- GZip Compression
""",
    version=settings.APP_VERSION,
    terms_of_service="https://example.com/terms",
    contact={
        "name": "Rahul Charan",
        "email": "rahul@example.com",
    },
    license_info={
        "name": "MIT License",
    },
    lifespan=lifespan,
)

# -------------------------
# Middleware
# -------------------------

app.add_middleware(RequestLoggerMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000
)

# -------------------------
# Exception Handler
# -------------------------

app.add_exception_handler(APIException, api_exception_handler)

# -------------------------
# Routers
# -------------------------

app.include_router(home_router, prefix=settings.API_PREFIX)
app.include_router(health_router, prefix=settings.API_PREFIX)
app.include_router(prediction_router, prefix=settings.API_PREFIX)