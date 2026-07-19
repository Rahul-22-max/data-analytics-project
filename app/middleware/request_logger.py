import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.utils.logger import logger


class RequestLoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        logger.info(f"{request.method} {request.url.path}")

        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f"Completed in {process_time:.4f} seconds"
        )

        response.headers["X-Process-Time"] = str(process_time)

        return response