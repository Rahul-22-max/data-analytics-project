# Logistic Regression Results

## Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 80.41% |
| Precision | 65.71% |
| Recall    | 54.81% |
| F1 Score  | 59.77% |
| ROC-AUC   | 84.27% |

## Key Findings

The Logistic Regression model achieved an accuracy of 80.41% and a ROC-AUC score of 84.27%, indicating strong discrimination between churned and non-churned customers.

The model correctly identified 205 churned customers while missing 169 churned customers. Improving recall will be a key focus in subsequent model optimization stages.

## Important Features

Features associated with lower churn probability:

* Contract_Two year
* Contract_One year
* PhoneService_Yes
* OnlineSecurity_Yes
* TechSupport_Yes

Features associated with higher churn probability:

* InternetService_Fiber optic
* PaymentMethod_Electronic check
* PaperlessBilling_Yes
* MultipleLines_Yes

## Conclusion

The Logistic Regression model provides a strong baseline for churn prediction. Future work will focus on hyperparameter tuning and tree-based ensemble methods such as Random Forest to improve recall and overall F1-score.
