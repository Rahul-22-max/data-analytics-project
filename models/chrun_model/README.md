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

## Day 8 Progress

- Implemented batch prediction pipeline
- Loaded saved churn prediction model
- Generated churn predictions for all customers
- Calculated churn probability scores
- Exported predictions to CSV
- Created batch prediction report

### Output

Generated file:

Data/processed/churn_predictions.csv

### Business Value

- Identify high-risk customers
- Support customer retention campaigns
- Enable large-scale churn scoring
- Prepare predictions for dashboards and reporting

## Day 9 Progress

- Implemented prediction analytics pipeline
- Segmented customers into churn risk groups
- Generated customer risk summary
- Calculated risk distribution percentages
- Exported analytics results to CSV
- Added business recommendations for retention strategies

### Risk Distribution

| Category | Customers |
|----------|----------:|
| High Risk | 504 |
| Medium Risk | 1579 |
| Low Risk | 4960 |

## Day 10 Progress

- Built FastAPI deployment layer
- Loaded trained churn prediction model
- Created REST API endpoints
- Added prediction endpoint for churn inference
- Generated Swagger documentation
- Successfully deployed local API using Uvicorn

### API Endpoints

GET /

Returns API status.

POST /predict

Accepts customer data and returns:

- prediction
- churn_probability

### Deployment Status

API running successfully on:

http://127.0.0.1:8000

## Day 12 Progress

- Implemented API logging
- Logged prediction requests
- Logged churn prediction results
- Added error logging
- Created logging documentation
- Improved API monitoring

## Day 13 Progress

- Developed model_monitor.py to evaluate the saved Logistic Regression model.
- Computed Accuracy, Precision, Recall, F1 Score, ROC-AUC, and Confusion Matrix.
- Generated model_performance_report.md.
- Exported evaluation metrics to model_metrics.csv.
- Improved model monitoring and reporting capabilities.

## Day 14 Progress

- Implemented model versioning utility.
- Archived trained models with version numbers.
- Created model registry.
- Stored training metadata.
- Prevented overwriting of previous models.
- Improved model lifecycle management.

## Day 15 Progress

- Developed an automated model retraining pipeline.
- Integrated model training, evaluation, versioning, and reporting.
- Automated execution of the complete machine learning workflow.
- Reduced manual execution steps.
- Improved project maintainability and reproducibility.

