# Day 8 - Model Evaluation

## Objective
Evaluate the Linear Regression model trained for LTV prediction.

## Metrics Used

### 1. MAE (Mean Absolute Error)
Measures the average absolute difference between predicted and actual LTV.

### 2. MSE (Mean Squared Error)
Measures squared prediction error and penalizes large mistakes.

### 3. RMSE (Root Mean Squared Error)
Square root of MSE; easier to interpret because it is in the same units as LTV.

### 4. R² Score
Measures how much variance in LTV is explained by the model.

## Evaluation Results
- MAE: <fill from notebook>
- MSE: <fill from notebook>
- RMSE: <fill from notebook>
- R² Score: <fill from notebook>

## Interpretation
- Lower MAE, MSE, RMSE are better.
- Higher R² is better.
- This baseline evaluation will be used to compare future models.


## Day 8 Conclusion

The Linear Regression model was evaluated using MAE, MSE, RMSE, and R² Score.

Key observations:
- MAE shows the average prediction error.
- MSE and RMSE show how strongly large errors affect the model.
- R² indicates how much of LTV variation is explained by the model.

This evaluation establishes a baseline for comparing more advanced models such as Random Forest and XGBoost.

## Day 8 Progress

- Evaluated Linear Regression model
- Calculated MAE, MSE, RMSE, and R² Score
- Compared actual vs predicted LTV
- Visualized residual errors
- Documented baseline model performance