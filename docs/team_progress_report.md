# Team Progress Report

## Project Title

Customer Churn Prediction & Customer Lifetime Value (LTV) Engine

---

## Team Members and Roles

### Member 1: Data Engineering & Data Warehouse Setup

**Responsibilities:**

* Dataset collection
* Data ingestion
* Repository setup
* Dataset documentation

**Status:**

* Completed initial dataset setup
* Uploaded raw dataset
* Created project structure
* Added dataset documentation

**Status:** ✅ Completed

---

### Member 2 (Team Lead): Exploratory Data Analysis & Feature Engineering

**Responsibilities:**

* Data cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Business insights generation
* Visualization and reporting
* Correlation analysis
* Correlation visualization
* Feature selection
* Machine Learning preparation
* Train-test split
* Machine Learning model development
* Logistic Regression model training
* Decision Tree model training
* Random Forest model training
* Model evaluation
* Model comparison
* Model selection
* Model serialization
* Prediction pipeline development
* API development

**Status:**

* Completed data preprocessing and feature engineering
* Performed Exploratory Data Analysis (EDA)
* Generated business insights and visualizations
* Performed correlation analysis
* Selected important features for machine learning
* Created train-test split
* Trained Logistic Regression model
* Trained Decision Tree model
* Trained Random Forest model
* Compared all machine learning models
* Selected Decision Tree as the best model
* Saved model using Joblib
* Built prediction pipeline
* Created Flask API
* Created `/health` endpoint
* Created `/predict` endpoint
* Implemented model inference through API
* Tested API using Postman
* Created all project documentation
* Updated final README
* Generated requirements.txt
* Prepared project for final submission

**Status:** ✅ Day 15 Completed

---

### Member 3: Core ML Engineering (Churn Prediction)

**Assigned To:** Prakalya G.B

**Responsibilities:**

* Model training
* Model evaluation
* Churn prediction pipeline

**Status:**

* Logistic Regression model completed
* Decision Tree model completed
* Random Forest model completed
* Model comparison completed
* Best model selected
* Prediction pipeline completed
* Flask API integration completed
* API testing completed

**Status:** ✅ Completed

---

### Member 4: Lifetime Value (LTV) Modeling & Model Explainability

**Assigned To:** Sri Veena Tejaswini

**Responsibilities:**

* Customer Lifetime Value prediction
* Model explainability
* Business interpretation

**Status:**

* Awaiting future implementation
* Initial planning completed

**Status:** ⏳ Future Enhancement

---

### Member 5: API Layer Development & Business Dashboards

**Assigned To:** Hariom Pandey

**Responsibilities:**

* API development
* Dashboard creation
* Visualization layer

**Status:**

* Flask API completed
* Health endpoint completed
* Prediction endpoint completed
* Postman testing completed
* Ready for dashboard integration

**Status:** 🟡 Ready for Next Phase

---

## Current Project Status

### Completed

* Dataset setup
* Repository and branch setup
* Data preprocessing
* Feature engineering
* Exploratory Data Analysis (EDA)
* Correlation analysis
* Feature selection
* Machine Learning preparation
* Logistic Regression model training
* Decision Tree model training
* Random Forest model training
* Model comparison
* Model selection
* Model saving using `joblib`
* Prediction pipeline creation
* Flask API development
* Health endpoint creation
* Prediction endpoint creation
* API testing using Postman
* Requirements file creation
* Final README update
* Project validation and cleanup
* Generated `day8_model_training.md`
* Generated `day9_model_comparison.md`
* Generated `day10_random_forest.md`
* Generated `day11_model_selection.md`
* Generated `day12_prediction_pipeline.md`
* Generated `day14_api_prediction.md`
* Saved model: `saved_models/churn_prediction_model.pkl`
* Saved feature columns: `saved_models/model_columns.pkl`
* README and project documentation updates

### In Progress

* None

### Pending

* Customer Lifetime Value (LTV) model (Future Enhancement)
* Dashboard development (Future Enhancement)
* Cloud deployment (Future Enhancement)

---

## Key Results

* Total Customers: **7043**
* Customers Stayed: **5174**
* Customers Churned: **1869**
* Processed Dataset Shape: **(7043, 32)**
* Features Before Encoding: **31**
* Features After Encoding: **33**
* Training Set Shape: **(5634, 33)**
* Testing Set Shape: **(1409, 33)**

### Model Performance

| Model               |     Accuracy |
| ------------------- | -----------: |
| Logistic Regression |   **80.06%** |
| Decision Tree       | **80.62%** ✅ |
| Random Forest       |   **80.41%** |

---

## Important Insights

* Gender has minimal effect on churn behavior.
* Customers with long-term contracts have significantly lower churn rates.
* New customers (0–1 Year tenure) have the highest churn risk.
* Churn decreases as customer tenure increases.
* Contract type and tenure are among the strongest churn indicators.
* Fiber optic internet users have a higher churn tendency.
* Electronic check payment method is positively correlated with churn.
* Decision Tree achieved the highest accuracy (**80.62%**) and was selected as the final model.
* The prediction pipeline successfully predicts churn for new customer data.
* Flask API successfully serves churn predictions.
* API accepts JSON input and returns predictions in real time.

---

## Day 15 Achievements

* Created `requirements.txt`
* Updated final project README
* Reviewed and validated project structure
* Completed final documentation review
* Finalized team progress report
* Prepared project demo flow
* Prepared project for submission
* Completed final project audit

---

## Final Project Status

✅ Data Analytics Workflow Completed

✅ Machine Learning Pipeline Completed

✅ Model Selection Completed

✅ Prediction Pipeline Completed

✅ Flask API Development Completed

✅ API Testing Completed

✅ Documentation Completed

✅ Project Ready for Submission

---

### Last Updated By:

**B. Rahul Charan Babu**

Team Lead & Member 2

**Project Day:** 15

**Overall Project Progress:** **100% Completed** ✅

**Project Status:** **Ready for Submission & Deployment** 🚀
