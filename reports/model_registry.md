# Model Registry

## Day 14 - Model Versioning

### Objective

Implemented model versioning to preserve trained models instead of overwriting them.

### Current Model

- Model: Logistic Regression
- Version: v1
- Accuracy: 80.41%
- ROC-AUC: 84.27%
- Training Date: 2026-07-21

### Files

Latest Model:
models/chrun_model/churn_model.pkl

Archived Model:
models/chrun_model/saved_models/churn_model_v1_20260721.pkl

Registry:
models/chrun_model/saved_models/model_registry.csv

### Benefits

- Maintains model history.
- Prevents accidental overwriting.
- Simplifies rollback to previous versions.
- Supports future retraining and comparison.