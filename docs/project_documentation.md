# Customer Churn Prediction & LTV Engine

## Project Overview

This project predicts Customer Churn and Customer Lifetime Value (LTV) using machine learning models. It also provides a FastAPI-based backend for serving predictions and includes SHAP explainability for model transparency.

---

## Objectives

- Predict customer churn
- Predict customer lifetime value
- Explain predictions using SHAP
- Provide REST API endpoints
- Segment customers based on predicted LTV

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- FastAPI
- Uvicorn
- Joblib
- Git
- GitHub

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Exploratory Data Analysis
5. Model Training
6. Model Evaluation
7. SHAP Explainability
8. Customer Segmentation
9. API Development
10. API Testing
11. Model Optimization
12. Final Testing

---

## Models Used

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

---

## Deployment Components

- FastAPI Backend
- Prediction Function
- Model Loader Utility
- JSON Payloads
- Testing Scripts

---

## Results

Include your final evaluation metrics:

- MAE
- MSE
- RMSE
- R² Score

---

## Future Improvements

- Deploy to Render or Railway
- Add authentication
- Create Streamlit dashboard
- Add database integration

# Customer Churn Prediction & LTV Engine

## Project Description

This project predicts Customer Lifetime Value (LTV) and Customer Churn using machine learning models. It includes explainability using SHAP and a FastAPI backend for serving predictions.

---

## Features

- Customer Churn Prediction
- Customer Lifetime Value Prediction
- SHAP Explainability
- Customer Segmentation
- FastAPI Backend
- REST API
- Sample JSON Payloads
- Model Optimization
- API Testing

---

## Technologies

- Python
- Scikit-learn
- XGBoost
- FastAPI
- SHAP
- Pandas
- NumPy
- Joblib

---

## Installation

```bash
git clone <repository-url>

cd customer-churn-ltv-engine

pip install -r requirements.txt
```

---

## Run the API

```bash
uvicorn backend.app.main:app --reload
```

---

## API Documentation

Open:

http://127.0.0.1:8000/docs

---

## Project Structure

Optimized tool selection## Project structure

- README.md
- requirements.txt
- backend
  - requirements.txt
  - `test_model_loader.py`
  - `test_payloads.py`
  - `test_prediction.py`
  - `app/`
    - `__init__.py`
    - `config.py`
    - `main.py`
    - `predictor.py`
    - `routes.py`
    - `schemas.py`
  - `samples/`
    - `average_customer.json`
    - `invalid_customer.json`
    - `low_value_customer.json`
    - `premium_customer.json`
- Data
  - `processed/`
    - `customer_ltv_v1.csv`
    - `customer_segments.csv`
    - `ltv_dataset.csv`
    - `ltv_prediction_validation.csv`
  - `raw/`
    - `Telco-Customer-Churn.csv`
- docs
  - `api_documentation.md`
  - `day1_notes.md`
  - `day10_xgboost_results.md`
  - `day11_12_model_selection.md`
  - `day13_15_shap_explainability.md`
  - `day16_shap_summary_plots.md`
  - `day19_ltv_validation.md`
  - `day2_revenue_findings.md`
  - `day20_customer_segmentation.md`
  - `day21_explainability_report.md`
  - `day22_model_loader.md`
  - `day23_api_integration.md`
  - `day24_prediction_function.md`
  - `day25_sample_payloads.md`
  - `day26_model_optimization.md`
  - `day27_final_testing.md`
  - `day3_ltv_strategy.md`
  - `day4_ltv_formula.md`
  - `day5_dataset_creation.md`
  - `day6_pipeline_setup.md`
  - `day7_linear_regression_results.md`
  - `day8_model_evaluation.md`
  - `day9_random_forest_results.md`
  - `installation_guide.md`
  - `project_documentation.md`
  - `project_summary.md`
  - `images/`
- explainability
  - `shap_explainer.py`
- models
- notebooks
  - `day1_dataset_understanding.ipynb`
  - `day10_xgboost_model.ipynb`
  - `day11_12_model_comparison.ipynb`
  - `day13_15_shap_explainability.ipynb`
  - `day16_shap_summary_plots.ipynb`
  - `day17_18_shap_waterfall_analysis.ipynb`
  - `day19_ltv_validation.ipynb`
  - `day2_revenue_analysis.ipynb`
  - `day20_customer_segmentation.ipynb`
  - `day22_model_loader_testing.ipynb`
  - `day26_model_optimization.ipynb`
  - `day3_ltv_target_selection.ipynb`
  - `day4_initial_ltv_calculation.ipynb`
  - `day5_create_ltv_dataset.ipynb`
  - `day6_regression_pipeline.ipynb`
  - `day7_linear_regression_model.ipynb`
  - `day8_model_evaluation.ipynb`
  - `day9_random_forest_model.ipynb`
- utils
  - `__init__.py`
  - `model_loader.py`

---

## Author

Gajjarapu Sri Veena Tejaswini