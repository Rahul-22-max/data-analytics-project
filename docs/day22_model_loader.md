# Day 22 - Model Loading Utility

## Objective

Create a reusable utility for loading trained machine learning models.

## Files Created

utils/model_loader.py

## Models Supported

- churn_model.pkl
- ltv_model.pkl
- linear_regression_ltv.pkl
- random_forest_ltv.pkl
- xgboost_ltv.pkl

## Features

- Centralized model loading
- Error handling for missing model files
- Reusable functions for all trained models

## Example

```python
from utils.model_loader import load_ltv_model

model = load_ltv_model()
```

## Benefits

- Cleaner code
- Easy backend integration
- Reusable across notebooks and APIs

## Day 22 Progress

- Created reusable model loading utility
- Added helper functions for all trained models
- Implemented error handling for missing model files
- Tested model loading successfully