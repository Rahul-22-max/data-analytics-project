# Team Progress Report

## Project Title

Customer Churn Prediction & Customer Lifetime Value (LTV) Engine

---

## Team Members and Roles

### Member 1: Data Engineering & Data Warehouse Setup

**Responsibilities:**

- Dataset collection
- Data ingestion
- Repository setup
- Dataset documentation

**Status:**

- Completed initial dataset setup
- Uploaded raw dataset
- Created project structure
- Added dataset documentation

**Status:** ✅ Completed

---

### Member 2 (Team Lead): Exploratory Data Analysis & Feature Engineering

**Responsibilities:**

- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Business insights generation
- Visualization and reporting
- Correlation analysis
- Correlation visualization
- Feature selection

**Status:**

- Converted `TotalCharges` to numeric format
- Handled missing values
- Created `TenureGroup` feature
- Encoded `gender` and `Churn` columns
- Removed `customerID`
- Generated processed dataset (`cleaned_telco_customer_churn.csv`)
- Performed churn distribution analysis
- Calculated churn rate by gender
- Calculated churn rate by contract type
- Calculated churn rate by tenure group
- Created visualization charts
- Generated `day2_business_insights.md`
- Generated `day4_business_insights.md`
- Performed correlation analysis with churn
- Created correlation visualization chart
- Identified top positive and negative churn features
- Selected important features for machine learning
- Generated `day6_feature_selection.md`
- Reviewed and validated processed dataset
- Prepared dataset for machine learning modeling
- Updated README and project documentation

**Status:** ✅ Day 6 Completed

---

### Member 3: Core ML Engineering (Churn Prediction)

**Assigned To:** Prakalya G.B

**Responsibilities:**

- Model training
- Model evaluation
- Churn prediction pipeline

**Status:**

- Received processed dataset from Member 2
- Ready to begin model development
- Feature selection completed
- Model training pending

**Status:** 🟡 Ready to Start

---

### Member 4: Lifetime Value (LTV) Modeling & Model Explainability

**Assigned To:** Sri Veena Tejaswini

**Responsibilities:**

- Customer Lifetime Value prediction
- Model explainability
- Business interpretation

**Status:**

- Awaiting churn model outputs
- Initial planning pending

**Status:** ⏳ Pending

---

### Member 5: API Layer Development & Business Dashboards

**Assigned To:** Hariom Pandey

**Responsibilities:**

- API development
- Dashboard creation
- Visualization layer

**Status:**

- Awaiting model outputs and predictions
- Dashboard framework planning pending

**Status:** ⏳ Pending

---

## Current Project Status

### Completed

- Dataset setup
- Repository and branch setup
- Data preprocessing
- Feature engineering
- Processed dataset generation
- Churn distribution analysis
- Churn analysis by gender
- Churn analysis by contract type
- Churn analysis by tenure group
- Business insights documentation
- Visualization charts
- Correlation analysis
- Correlation visualization
- Feature selection for ML
- Dataset validation for ML readiness
- README and project documentation updates

### In Progress

- Machine learning preparation
- Model development handoff to Member 3

### Pending

- Churn prediction model
- Model evaluation
- Customer Lifetime Value (LTV) model
- API development
- Dashboard development
- Model deployment pipeline

---

## Key Results

- Total Customers: **7043**
- Customers Stayed: **5174**
- Customers Churned: **1869**
- Processed Dataset Shape: **(7043, 32)**

### Important Insights

- Gender has minimal effect on churn behavior.
- Customers with long-term contracts have significantly lower churn rates.
- New customers (0–1 Year tenure) have the highest churn risk.
- Churn decreases as customer tenure increases.
- Contract type and tenure are among the strongest churn indicators identified during EDA.
- Fiber optic internet users have a higher churn tendency.
- Electronic check payment method is positively correlated with churn.

---

## Day 6 Achievements

- Completed correlation analysis with churn.
- Visualized feature correlations using bar charts.
- Identified top positive and negative churn factors.
- Selected important features for machine learning.
- Generated `day6_feature_selection.md`.
- Finalized EDA and feature engineering phase.
- Prepared dataset for model training.

---

## Next Milestone (Day 7)

- Member 3 to begin churn prediction model training.
- Perform train-test split.
- Train baseline machine learning models.
- Evaluate model performance metrics.
- Compare different algorithms.
- Prepare initial churn prediction pipeline.

---

### Last Updated By:

**B. Rahul Charan Babu**  
Team Lead & Member 2

**Project Day:** 6

**Overall Project Progress:** **50% Completed** ✅