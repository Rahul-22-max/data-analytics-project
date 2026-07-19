from fastapi import FastAPI

from app.core.config import settings
from app.core.exceptions import APIException, api_exception_handler

from app.middleware.request_logger import RequestLoggerMiddleware

from app.api.v1 import api_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Middleware
app.add_middleware(RequestLoggerMiddleware)

# Global Exception Handler
app.add_exception_handler(APIException, api_exception_handler)

# Routers
app.include_router(api_router)