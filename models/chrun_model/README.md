# Churn Prediction Module

## Day 1 Progress

- Created project structure
- Added data loading utility
- Added train/test split framework
- Added evaluation framework

## Day 2 Progress

- Created Python virtual environment
- Installed ML dependencies
- Generated requirements.txt
- Configured project environment

## Day 3 Progress

- Implemented Logistic Regression baseline model
- Loaded processed churn dataset
- Performed train/test split
- Generated predictions
- Evaluated model performance

Results:
- Accuracy: 80.55%
- Precision: 65.72%
- Recall: 55.88%
- F1 Score: 60.40%

Day 3 Status
Dataset loaded: ✅
Model trained: ✅
Predictions generated: ✅
Metrics calculated: ✅
Documentation updated: ⏳
Commit and push: ⏳



## Day 4 Progress

- Added model persistence using Joblib
- Saved trained model as churn_model.pkl
- Implemented Decision Tree baseline
- Compared Logistic Regression and Decision Tree performance

## Day 5 Progress

- Implemented Decision Tree classifier
- Implemented Random Forest classifier
- Compared Logistic Regression, Decision Tree and Random Forest
- Evaluated model performance using Accuracy and F1 Score
- Created model comparison report
- Selected Logistic Regression as the best-performing model

### Final Model Performance

| Model | Accuracy | F1 Score |
|---------|---------:|---------:|
| Logistic Regression | 80.41% | 59.77% |
| Decision Tree | 74.45% | 51.48% |
| Random Forest | 78.57% | 55.19% |

## Day 6 Progress

- Implemented feature importance analysis
- Extracted Logistic Regression coefficients
- Ranked customer attributes based on impact on churn
- Generated feature importance report
- Identified major churn drivers and retention factors

### Top Churn Drivers

- PaymentMethod_Electronic check
- PaperlessBilling_Yes
- MultipleLines_Yes

### Top Retention Factors

- Contract_One year
- OnlineSecurity_Yes
- TechSupport_Yes
- Dependents_Yes

## Day 7 Progress

- Implemented model inference pipeline
- Loaded saved Logistic Regression model using Joblib
- Generated predictions for new customer profiles
- Calculated churn probability scores
- Created inference documentation

### Sample Prediction

| Metric | Value |
|----------|----------|
| Prediction | 0 (No Churn) |
| Churn Probability | 21.06% |

### Outcome

The trained model successfully predicts customer churn risk and can be used for customer retention and risk scoring applications.