from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="Customer LTV Prediction API"
)

app.include_router(router)

@app.get("/")

def home():

    return {
        "message":
        "Customer LTV Prediction API Running"
    }

@app.get("/health")

def health():

    return {
        "status": "healthy"
    }