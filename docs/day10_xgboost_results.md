# Day 10 - XGBoost Regressor for LTV Prediction

## Objective
Train an XGBoost Regressor to predict Customer Lifetime Value (LTV).

## Dataset
Input file:
data/processed/ltv_dataset.csv

## Target Variable
LTV

## Model Used
XGBRegressor

## Preprocessing
- StandardScaler for numerical features
- OneHotEncoder for categorical features

## Train-Test Split
- 80% training
- 20% testing
- random_state = 42

## Model Parameters
- n_estimators = 100
- learning_rate = 0.1
- max_depth = 5
- random_state = 42
- objective = reg:squarederror

## Evaluation Metrics
- MAE: <fill from notebook>
- MSE: <fill from notebook>
- RMSE: <fill from notebook>
- R² Score: <fill from notebook>

## Comparison with Other Models
Compare XGBoost with:
- Linear Regression
- Random Forest Regressor

## Output Files
- notebooks/day10_xgboost_model.ipynb
- models/xgboost_ltv.pkl

## Day 10 Progress

- Installed and trained XGBoost Regressor
- Built preprocessing + XGBoost pipeline
- Evaluated model using MAE, MSE, RMSE, and R²
- Compared XGBoost with Linear Regression and Random Forest
- Saved trained XGBoost model