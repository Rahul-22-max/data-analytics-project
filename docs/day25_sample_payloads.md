# Day 25 - Sample JSON Payloads

## Objective

Create reusable JSON payloads for testing the Customer LTV Prediction API.

## Payload Files

- premium_customer.json
- average_customer.json
- low_value_customer.json
- invalid_customer.json

## Testing

Each payload was tested using:

- FastAPI Swagger UI
- Python requests

## Expected Results

| Payload | Expected Result |
|----------|-----------------|
| Premium Customer | High predicted LTV |
| Average Customer | Medium predicted LTV |
| Low Value Customer | Low predicted LTV |
| Invalid Customer | Validation error |

## Day 25 Progress

- Created reusable sample JSON payloads
- Added valid and invalid test cases
- Tested API using Swagger UI
- Added payload documentation