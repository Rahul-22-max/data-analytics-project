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

---

### Member 2 (Team Lead): Exploratory Data Analysis & Feature Engineering

**Responsibilities:**

* Data cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Business insights generation
* Visualization and reporting

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
* Created 5 visualization charts
* Generated `day2_business_insights.md`
* Generated `day4_business_insights.md`
* Updated README and project documentation

**Status:** ✅ Day 4 Completed

---

### Member 3: Core ML Engineering (Churn Prediction)

**Assigned To:** Prakalya G.B

**Responsibilities:**

* Model training
* Model evaluation
* Churn prediction pipeline

**Status:**

* Pending

---

### Member 4: Lifetime Value (LTV) Modeling & Model Explainability

**Assigned To:** Sri Veena Tejaswini

**Responsibilities:**

* Customer Lifetime Value prediction
* Model explainability
* Business interpretation

**Status:**

* Pending

---

### Member 5: API Layer Development & Business Dashboards

**Assigned To:** Hariom Pandey

**Responsibilities:**

* API development
* Dashboard creation
* Visualization layer

**Status:**

* Pending

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
* README documentation

### In Progress

* Advanced EDA improvements
* Preparing dataset for machine learning

### Pending

* Churn prediction model
* Customer Lifetime Value (LTV) model
* API development
* Dashboard development

---

## Key Results

* Total Customers: **7043**
* Customers Stayed: **5174**
* Customers Churned: **1869**
* Processed Dataset Shape: **(7043, 32)**

### Important Insights

* Gender has minimal effect on churn.
* Customers with long-term contracts have significantly lower churn.
* New customers (0-1 Year tenure) have the highest churn rate.
* Churn decreases as customer tenure increases.

---

## Next Milestone

* Complete advanced EDA and visualizations
* Prepare dataset for ML modeling
* Start churn prediction model development
* Begin Member 3 model training tasks

---

**Last Updated By:**
**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 4
