from fastapi import FastAPI

from app.core.config import settings
from app.core.exceptions import global_exception_handler

from app.routes.home import router as home_router
from app.routes.prediction import router as prediction_router

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(home_router)
app.include_router(prediction_router)