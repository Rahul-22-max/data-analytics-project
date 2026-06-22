# Day 7 - Linear Regression for LTV Prediction

## Objective
Train a baseline Linear Regression model to predict Customer Lifetime Value (LTV).

## Dataset
Input file:
data/processed/ltv_dataset.csv

## Target Variable
LTV

## Model Used
Linear Regression

## Preprocessing
- StandardScaler for numerical columns
- OneHotEncoder for categorical columns

## Train-Test Split
- 80% training
- 20% testing
- random_state = 42

## Evaluation Metrics
- MAE: <fill from notebook>
- MSE: <fill from notebook>
- RMSE: <fill from notebook>
- R² Score: <fill from notebook>

## Observations
- Linear Regression serves as a baseline model.
- It helps estimate how well basic customer attributes explain LTV.
- Future models like Random Forest and XGBoost may improve performance.

## Output Files
- notebooks/day7_linear_regression_model.ipynb
- models/linear_regression_ltv.pkl

## Day 7 Progress

- Trained first baseline regression model
- Built full preprocessing + Linear Regression pipeline
- Predicted LTV on test data
- Evaluated model with MAE, RMSE, and R²
- Saved trained model