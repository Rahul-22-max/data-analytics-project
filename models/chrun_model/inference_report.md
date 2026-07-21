# Model Inference Report

## Objective

Use the trained churn prediction model to predict whether a new customer is likely to churn.

## Input

Customer profile features generated from the preprocessing pipeline.

## Output

- Churn Prediction (0 or 1)
- Churn Probability

## Model Used

- Logistic Regression
- Saved as `churn_model.pkl`

## Use Cases

- Customer retention campaigns
- Risk scoring
- Customer support prioritization

# Model Inference Report

## Objective

Use the trained churn prediction model to predict whether a customer is likely to churn.

## Sample Prediction

Prediction: 0

Churn Probability: 21.06%

## Interpretation

The sample customer is predicted to remain with the company.

A churn probability of 21.06% indicates relatively low churn risk.

## Model Used

- Logistic Regression
- Accuracy: 80.41%
- F1 Score: 59.77%
- Saved Model: churn_model.pkl

## Use Cases

- Customer retention campaigns
- Risk scoring
- Personalized offers
- Customer success prioritization