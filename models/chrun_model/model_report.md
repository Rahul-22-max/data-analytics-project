# Model Comparison Report

## Model Performance

| Model | Accuracy | F1 Score |
|---------|---------:|---------:|
| Logistic Regression | 80.41% | 59.77% |
| Decision Tree | 74.45% | 51.48% |
| Random Forest | 78.57% | 55.19% |

## Selected Model

Logistic Regression was selected as the preferred model because it achieved the highest Accuracy and F1 Score among all evaluated models.

## Conclusion

- Logistic Regression demonstrated the best overall classification performance.
- Random Forest provided competitive results but did not outperform Logistic Regression.
- Decision Tree showed lower predictive performance compared to the other models.

The Logistic Regression model was retained and saved as `churn_model.pkl` for future deployment and inference.