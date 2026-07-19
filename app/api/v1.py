from fastapi import APIRouter

from app.routes.home import router as home_router
from app.routes.health import router as health_router
from app.routes.prediction import router as prediction_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(home_router)
api_router.include_router(health_router)
api_router.include_router(prediction_router)