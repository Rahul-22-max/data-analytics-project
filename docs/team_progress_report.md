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

**Status:**

* Converted `TotalCharges` to numeric format
* Handled missing values
* Created `TenureGroup` feature
* Encoded `gender` and `Churn` columns
* Removed `customerID`
* Generated processed dataset (`cleaned_telco_customer_churn.csv`)
* Performed churn distribution analysis
* Calculated churn rate by gender
* Calculated churn rate by contract type
* Calculated churn rate by tenure group
* Created visualization charts
* Generated `day2_business_insights.md`
* Generated `day4_business_insights.md`
* Performed correlation analysis with churn
* Created correlation visualization chart
* Identified top positive and negative churn features
* Selected important features for machine learning
* Generated `day6_feature_selection.md`
* Created train-test split using 80:20 ratio
* Prepared features (`X`) and target (`y`)
* Applied one-hot encoding to categorical features
* Generated `day7_ml_preparation.md`
* Created `logistic_regression_model.py`
* Trained Logistic Regression model (**80.06%** accuracy)
* Generated `day8_model_training.md`
* Created `decision_tree_model.py`
* Trained Decision Tree Classifier (**80.62%** accuracy)
* Generated `day9_model_comparison.md`
* Created `random_forest_model.py`
* Trained Random Forest Classifier (**80.41%** accuracy)
* Generated `day10_random_forest.md`
* Created `model_comparison.py`
* Compared all machine learning models
* Selected **Decision Tree** as the final best model
* Created `save_model.py`
* Saved model as `saved_models/churn_prediction_model.pkl`
* Generated `day11_model_selection.md`
* Created `predict.py`
* Loaded saved model successfully
* Built prediction pipeline for new customer data
* Successfully predicted churn for sample customer
* Generated `day12_prediction_pipeline.md`
* Updated README and project documentation

**Status:** ✅ Day 12 Completed

---

### Member 3: Core ML Engineering (Churn Prediction)

**Assigned To:** Prakalya G.B

**Responsibilities:**

* Model training
* Model evaluation
* Churn prediction pipeline

**Status:**

* Received processed dataset from Member 2
* Logistic Regression model completed
* Decision Tree model completed
* Random Forest model completed
* Model comparison completed
* Best model selected: **Decision Tree**
* Model saved successfully
* Prediction pipeline completed
* Model ready for API deployment

**Status:** 🟡 In Progress

---

### Member 4: Lifetime Value (LTV) Modeling & Model Explainability

**Assigned To:** Sri Veena Tejaswini

**Responsibilities:**

* Customer Lifetime Value prediction
* Model explainability
* Business interpretation

**Status:**

* Awaiting final churn model outputs
* Initial planning pending

**Status:** ⏳ Pending

---

### Member 5: API Layer Development & Business Dashboards

**Assigned To:** Hariom Pandey

**Responsibilities:**

* API development
* Dashboard creation
* Visualization layer

**Status:**

* Saved model available
* Prediction pipeline completed
* Ready to start API development

**Status:** 🟡 Ready to Start

---

## Current Project Status

### Completed

* Dataset setup
* Repository and branch setup
* Data preprocessing
* Feature engineering
* Processed dataset generation
* Churn distribution analysis
* Churn analysis by gender
* Churn analysis by contract type
* Churn analysis by tenure group
* Business insights documentation
* Visualization charts
* Correlation analysis
* Correlation visualization
* Feature selection for ML
* Machine Learning preparation
* Train-test split
* Logistic Regression model training
* Decision Tree model training
* Random Forest model training
* Model evaluation
* Model comparison
* Model selection
* Model saving using `joblib`
* Prediction pipeline creation
* Generated `day8_model_training.md`
* Generated `day9_model_comparison.md`
* Generated `day10_random_forest.md`
* Generated `day11_model_selection.md`
* Generated `day12_prediction_pipeline.md`
* Saved model: `saved_models/churn_prediction_model.pkl`
* Dataset validation for ML readiness
* README and project documentation updates

### In Progress

* API deployment preparation
* Dashboard planning

### Pending

* Customer Lifetime Value (LTV) model
* API development
* Dashboard development
* Model deployment pipeline

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

### Important Insights

* Gender has minimal effect on churn behavior.
* Customers with long-term contracts have significantly lower churn rates.
* New customers (0–1 Year tenure) have the highest churn risk.
* Churn decreases as customer tenure increases.
* Contract type and tenure are among the strongest churn indicators identified during EDA.
* Fiber optic internet users have a higher churn tendency.
* Electronic check payment method is positively correlated with churn.
* Decision Tree achieved the highest accuracy (**80.62%**) and was selected as the final model.
* The prediction pipeline successfully predicts churn for new customer data.
* The project is now ready for API deployment.

---

## Day 12 Achievements

* Created `predict.py`.
* Loaded saved Decision Tree model.
* Built prediction pipeline.
* Predicted churn for sample customer data.
* Generated `day12_prediction_pipeline.md`.
* Prepared project for API integration and deployment.

---

## Next Milestone (Day 13)

* Build API using Flask.
* Create `/predict` endpoint.
* Create `/health` endpoint.
* Accept customer data as JSON.
* Return churn predictions through API.
* Test API using Postman.

---

### Last Updated By:

**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 12

**Overall Project Progress:** **95% Completed** ✅
