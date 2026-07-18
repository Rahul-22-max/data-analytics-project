# API Documentation

## GET /

Returns API status.

---

## GET /health

Returns application health.

---

## POST /predict

Predicts Customer Lifetime Value.

### Input

Customer details in JSON format.

### Output

Predicted Customer Lifetime Value.

Example:

```json
{
  "success": true,
  "predicted_ltv": 2894.12
}
```

## Screenshots

- Swagger API
- SHAP Summary Plot
- Customer Segmentation
- Model Evaluation