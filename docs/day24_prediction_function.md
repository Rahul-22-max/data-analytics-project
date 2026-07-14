# Day 24 - Prediction Function

## Objective

Create a reusable prediction function for the FastAPI backend.

## File Created

backend/app/predictor.py

## Function

predict_ltv(customer_data)

## Features

- Loads trained LTV model
- Accepts customer information
- Returns predicted Customer Lifetime Value
- Handles prediction errors gracefully

## Testing

- Tested with valid customer data
- Tested with invalid input
- Verified API integration

## Output Example

```json
{
  "success": true,
  "predicted_ltv": 2847.63
}
```

## Day 24 Progress

- Created reusable prediction function
- Added error handling
- Integrated prediction logic with FastAPI
- Tested predictions successfully