from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.lifespan import lifespan
from app.core.exceptions import APIException, api_exception_handler
from app.middleware.request_logger import RequestLoggerMiddleware
from app.api.v1 import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

# -----------------------------
# CORS Configuration
# -----------------------------
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request Logger Middleware
# -----------------------------
app.add_middleware(RequestLoggerMiddleware)

# -----------------------------
# Exception Handler
# -----------------------------
app.add_exception_handler(APIException, api_exception_handler)

# -----------------------------
# API Routes
# -----------------------------
app.include_router(api_router)