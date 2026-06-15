Project Title
Customer Churn Prediction & Customer Lifetime Value (LTV) Engine
Team Members and Roles
Member 1: Data Engineering & Data Warehouse Setup
Responsibilities:
Dataset collection
Data ingestion
Repository setup
Dataset documentation
Status:
Completed initial dataset setup
Uploaded raw dataset
Created project structure
Added dataset documentation
Status: ✅ Completed
Member 2 (Team Lead): Exploratory Data Analysis & Feature Engineering
Responsibilities:
Data cleaning
Exploratory Data Analysis (EDA)
Feature engineering
Business insights generation
Visualization and reporting
Status:
Converted TotalCharges to numeric format
Handled missing values
Created TenureGroup feature
Encoded gender and Churn columns
Removed customerID
Generated processed dataset (cleaned_telco_customer_churn.csv)
Performed churn distribution analysis
Calculated churn rate by gender
Calculated churn rate by contract type
Calculated churn rate by tenure group
Created visualization charts
Generated day2_business_insights.md
Generated day4_business_insights.md
Reviewed and validated processed dataset
Prepared dataset for machine learning modeling
Updated README and project documentation
Status: ✅ Day 5 Completed
Member 3: Core ML Engineering (Churn Prediction)
Assigned To: Prakalya G.B
Responsibilities:
Model training
Model evaluation
Churn prediction pipeline
Status:
Received processed dataset from Member 2
Ready to begin model development
Feature selection and model planning pending
Status: 🟡 Ready to Start
Member 4: Lifetime Value (LTV) Modeling & Model Explainability
Assigned To: Sri Veena Tejaswini
Responsibilities:
Customer Lifetime Value prediction
Model explainability
Business interpretation
Status:
Awaiting churn model outputs
Initial planning pending
Status: ⏳ Pending
Member 5: API Layer Development & Business Dashboards
Assigned To: Hariom Pandey
Responsibilities:
API development
Dashboard creation
Visualization layer
Status:
Awaiting model outputs and predictions
Dashboard framework planning pending
Status: ⏳ Pending
Current Project Status
Completed
Dataset setup
Repository and branch setup
Data preprocessing
Feature engineering
Processed dataset generation
Churn distribution analysis
Churn analysis by gender
Churn analysis by contract type
Churn analysis by tenure group
Business insights documentation
Visualization charts
Dataset validation for ML readiness
README and project documentation updates
In Progress
Machine learning preparation
Model development handoff to Member 3
Pending
Churn prediction model
Model evaluation
Customer Lifetime Value (LTV) model
API development
Dashboard development
Model deployment pipeline
Key Results
Total Customers: 7043
Customers Stayed: 5174
Customers Churned: 1869
Processed Dataset Shape: (7043, 32)
Important Insights
Gender has minimal effect on churn behavior.
Customers with long-term contracts have significantly lower churn rates.
New customers (0–1 Year tenure) have the highest churn risk.
Churn decreases as customer tenure increases.
Contract type and tenure are among the strongest churn indicators identified during EDA.
Day 5 Achievements
Finalized EDA findings and business insights.
Validated processed dataset quality.
Confirmed dataset readiness for machine learning.
Completed documentation updates and reporting.
Successfully handed over processed dataset to Member 3 for churn prediction model development.
Next Milestone (Day 6)
Member 3 to begin churn prediction model training.
Perform train-test split and feature selection.
Evaluate baseline machine learning models.
Compare model performance metrics.
Prepare initial churn prediction pipeline.
Last Updated By:
B. Rahul Charan Babu
Team Lead & Member 2
Project Day: 5
Overall Project Progress: 40% Completed ✅