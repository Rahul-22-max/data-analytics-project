from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.config import settings
from app.core.exceptions import (
    APIException,
    api_exception_handler,
    not_found_handler,
)

from app.middleware.request_logger import RequestLoggerMiddleware

from app.routes.home import router as home_router
from app.routes.health import router as health_router
from app.routes.prediction import router as prediction_router
from app.routes.info import router as info_router
from app.routes.metrics import router as metrics_router
from app.routes.version import router as version_router

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

Production-ready FastAPI application.

### Features

- Customer Churn Prediction
- Health Check
- API Information
- Application Metrics
- Version Endpoint
- Request Logging
- CORS
- GZip Compression
- Custom Exception Handling
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

# ======================================================
# Middleware
# ======================================================

# Request Logger
app.add_middleware(RequestLoggerMiddleware)

# CORS
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

# GZip Compression
app.add_middleware(
    GZipMiddleware,
    minimum_size=1000,
)

# ======================================================
# Exception Handlers
# ======================================================

app.add_exception_handler(APIException, api_exception_handler)

app.add_exception_handler(
    StarletteHTTPException,
    not_found_handler
)

# ======================================================
# Routers
# ======================================================

app.include_router(home_router, prefix=settings.API_PREFIX)
app.include_router(health_router, prefix=settings.API_PREFIX)
app.include_router(prediction_router, prefix=settings.API_PREFIX)
app.include_router(info_router, prefix=settings.API_PREFIX)
app.include_router(metrics_router, prefix=settings.API_PREFIX)
app.include_router(version_router, prefix=settings.API_PREFIX)