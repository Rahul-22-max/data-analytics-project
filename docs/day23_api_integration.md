# Day 23 - API Integration

## Objective

Create and test a FastAPI service for Customer Lifetime Value prediction.

## Endpoints

### GET /

Returns API status.

### GET /health

Checks API health.

### POST /predict

Predicts Customer Lifetime Value.

## Input

Customer information.

## Output

Predicted LTV.

## Testing

The API was tested using Swagger UI.

All endpoints returned successful responses.

## Models Used

ltv_model.pkl

## Day 23 Progress

- Built FastAPI backend
- Integrated trained LTV model
- Added prediction endpoint
- Added health check endpoint
- Tested API using Swagger UI