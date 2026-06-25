# Customer Churn Prediction & Customer Lifetime Value (LTV) Engine

## Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses. This project focuses on analyzing customer behavior, identifying churn patterns, and building a machine learning solution to predict whether a customer is likely to leave the company.

The project follows a complete Data Analytics and Machine Learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model development, model deployment preparation, and API integration.

---

## Problem Statement

Businesses lose revenue when customers discontinue their services. Identifying customers who are likely to churn allows organizations to take proactive retention measures.

This project aims to:

* Predict customer churn using machine learning.
* Generate business insights from customer behavior.
* Provide real-time churn predictions through a Flask API.
* Prepare the foundation for Customer Lifetime Value (LTV) analysis.

---

## Dataset Information

**Dataset:** Telco Customer Churn Dataset

The dataset contains information about:

* Customer demographics
* Subscription services
* Contract details
* Internet services
* Payment methods
* Monthly charges
* Total charges
* Customer churn status

### Dataset Statistics

* Total Customers: **7043**
* Customers Stayed: **5174**
* Customers Churned: **1869**
* Processed Dataset Shape: **(7043, 32)**

---

## Technology Stack

* Python 3.12
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Flask
* Joblib
* Git & GitHub
* VS Code
* Postman

---

## Project Workflow

### Phase 1: Data Preparation

* Dataset loading
* Data cleaning
* Missing value handling
* Feature engineering
* Data transformation

### Phase 2: Exploratory Data Analysis

* Churn distribution analysis
* Gender-based churn analysis
* Contract type analysis
* Tenure analysis
* Correlation analysis
* Business insight generation

### Phase 3: Machine Learning

* Train-Test Split
* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* Model Evaluation
* Model Comparison
* Best Model Selection

### Phase 4: Model Deployment Preparation

* Model Saving using Joblib
* Prediction Pipeline Development
* Flask API Development
* Postman API Testing

---

## Machine Learning Models

| Model               | Accuracy |
| ------------------- | -------: |
| Logistic Regression |   80.06% |
| Decision Tree       |   80.62% |
| Random Forest       |   80.41% |

### Best Model

**Decision Tree Classifier**

Accuracy: **80.62%**

The Decision Tree model achieved the highest accuracy and was selected as the final churn prediction model.

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
    "status": "API Running Successfully"
}
```

### Churn Prediction

```http
POST /predict
```

Sample Request:

```json
{
    "gender": 0,
    "SeniorCitizen": 0,
    "tenure": 1,
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85
}
```

Sample Response:

```json
{
    "prediction": "Customer is likely to CHURN"
}
```

---

## Project Structure

```text
DATA-ANALYTICS-PROJECT/

api/
├── app.py

data/
├── raw/
└── processed/

docs/
├── dataset_description.md
├── day11_model_selection.md
├── day12_prediction_pipeline.md
├── day14_api_prediction.md
├── team_progress_report.md

eda/
├── churn_analysis.py
├── churn_visualization.py
├── correlation_analysis.py
├── correlation_visualization.py
├── feature_engineering.py

models/
├── logistic_regression_model.py
├── decision_tree_model.py
├── random_forest_model.py
├── model_comparison.py
├── save_model.py
├── predict.py

saved_models/
├── churn_prediction_model.pkl
├── model_columns.pkl

README.md
requirements.txt
```

---

## Key Business Insights

* Gender has minimal impact on churn behavior.
* Customers with month-to-month contracts have higher churn rates.
* Long-term contract customers are less likely to churn.
* New customers show higher churn risk.
* Churn decreases as tenure increases.
* Fiber optic customers demonstrate higher churn tendencies.
* Electronic check users are more likely to churn.

---

## Team Members

| Role      | Name                 |
| --------- | -------------------- |
| Team Lead | B. Rahul Charan Babu |
| Member 1  | S. Mohamed Javeeth   |
| Member 2  | B. Rahul Charan Babu |
| Member 3  | Prakalya G B         |
| Member 4  | Hariom Pandey        |
| Member 5  | Sri Veena Tejaswini  |

---

## Project Status

✅ Data Cleaning Completed

✅ Exploratory Data Analysis Completed

✅ Feature Engineering Completed

✅ Machine Learning Model Development Completed

✅ Model Comparison Completed

✅ Model Selection Completed

✅ Prediction Pipeline Completed

✅ Flask API Development Completed

✅ Postman Testing Completed

✅ Documentation Completed

✅ Project Ready for Submission

---

## Future Enhancements

* Customer Lifetime Value (LTV) Prediction
* Interactive Dashboard Development
* Cloud Deployment
* Real-Time Customer Monitoring
* Automated Retraining Pipeline

---

## Author

**B. Rahul Charan Babu**

Team Lead & Data Analytics Student

Project Version: **1.0**

Status: **100% Completed**
