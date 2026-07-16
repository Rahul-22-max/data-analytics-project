from fastapi import FastAPI

app = FastAPI(
    title="Customer Churn & LTV Prediction API",
    description="Backend API for Customer Churn Prediction and Lifetime Value Estimation",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Customer Churn & LTV Prediction API is running!",
        "version": "1.0.0"
    }