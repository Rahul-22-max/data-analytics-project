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
* Trained Logistic Regression model
* Achieved **80.06%** model accuracy
* Generated confusion matrix and classification report
* Removed convergence warning using `solver="liblinear"`
* Generated `day8_model_training.md`
* Created `decision_tree_model.py`
* Trained Decision Tree Classifier
* Achieved **80.62%** model accuracy
* Compared Logistic Regression and Decision Tree models
* Generated `day9_model_comparison.md`
* Created `random_forest_model.py`
* Trained Random Forest Classifier
* Achieved **80.41%** model accuracy
* Compared Random Forest with Logistic Regression and Decision Tree
* Generated `day10_random_forest.md`
* Identified Decision Tree as the current best model
* Prepared dataset for churn prediction model development
* Reviewed and validated processed dataset
* Updated README and project documentation

**Status:** ✅ Day 10 Completed

---

### Member 3: Core ML Engineering (Churn Prediction)

**Assigned To:** Prakalya G.B

**Responsibilities:**

* Model training
* Model evaluation
* Churn prediction pipeline

**Status:**

* Received processed dataset from Member 2
* Received train-test split dataset
* Logistic Regression model completed
* Decision Tree model completed
* Random Forest model completed
* Model comparison completed
* Best model selection pending

**Status:** 🟡 In Progress

---

### Member 4: Lifetime Value (LTV) Modeling & Model Explainability

**Assigned To:** Sri Veena Tejaswini

**Responsibilities:**

* Customer Lifetime Value prediction
* Model explainability
* Business interpretation

**Status:**

* Awaiting final churn model
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

* Awaiting final model outputs
* Dashboard framework planning pending

**Status:** ⏳ Pending

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
* Generated `day8_model_training.md`
* Generated `day9_model_comparison.md`
* Generated `day10_random_forest.md`
* Dataset ready for churn prediction model
* Dataset validation for ML readiness
* README and project documentation updates

### In Progress

* Final model selection
* Model serialization and deployment preparation

### Pending

* Save best model using `joblib`
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
* Decision Tree currently performs best with **80.62% accuracy**.
* Random Forest provides stable predictions with **80.41% accuracy**.

---

## Day 10 Achievements

* Trained Random Forest Classifier.
* Achieved **80.41%** prediction accuracy.
* Generated confusion matrix and classification report.
* Compared Random Forest with Logistic Regression and Decision Tree.
* Created `day10_random_forest.md`.
* Identified Decision Tree as the current best model.

---

## Next Milestone (Day 11)

* Compare all machine learning models in detail.
* Select the final best model.
* Save the trained model using `joblib`.
* Prepare model for API deployment.
* Begin prediction pipeline development.

---

### Last Updated By:

**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 10

**Overall Project Progress:** **85% Completed** ✅
