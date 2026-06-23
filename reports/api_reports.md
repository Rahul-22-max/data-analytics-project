# Prediction API Report

## Objective

Expose the trained churn prediction model as a REST API.

## Technology Stack

- FastAPI
- Uvicorn
- Joblib
- Scikit-Learn

## Endpoints

### GET /

Returns service status.

### POST /predict

Accepts customer attributes and returns:

- Churn prediction
- Churn probability

## Deployment Result

API successfully launched and tested locally.

## Business Applications

- Power BI integration
- Web application integration
- CRM integration
- Real-time churn scoring