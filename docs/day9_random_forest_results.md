# Day 9 - Random Forest Regressor for LTV Prediction

## Objective
Train a Random Forest Regressor to predict Customer Lifetime Value (LTV).

## Dataset
Input file:
data/processed/ltv_dataset.csv

## Target Variable
LTV

## Model Used
RandomForestRegressor

## Preprocessing
- StandardScaler for numerical features
- OneHotEncoder for categorical features

## Train-Test Split
- 80% training
- 20% testing
- random_state = 42

## Model Parameters
- n_estimators = 100
- random_state = 42

## Evaluation Metrics
- MAE: <fill from notebook>
- MSE: <fill from notebook>
- RMSE: <fill from notebook>
- R² Score: <fill from notebook>

## Comparison with Linear Regression
Summarize whether Random Forest improved the model performance.

## Output Files
- notebooks/day9_random_forest_model.ipynb
- models/random_forest_ltv.pkl

## Day 9 Progress

- Trained Random Forest Regressor for LTV prediction
- Evaluated model using MAE, MSE, RMSE, and R²
- Compared Random Forest with Linear Regression baseline
- Saved trained Random Forest model