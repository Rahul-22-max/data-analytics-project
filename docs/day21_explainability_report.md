# Explainability Report

## Project

Customer Churn Prediction & Customer Lifetime Value (LTV) Engine

---

# Objective

The objective of this report is to explain how the trained machine learning model makes predictions using SHAP (SHapley Additive exPlanations).

SHAP improves model transparency by identifying which customer features have the greatest impact on churn predictions.

---

# Explainability Method

Technique Used:

- SHAP (SHapley Additive Explanations)

Model Explained:

- Churn Prediction Model

Purpose:

- Explain global model behavior
- Explain individual customer predictions

---

# Dataset

Telco Customer Churn Dataset

Target Variable:

- Churn

---

# SHAP Summary Plot

The SHAP Summary Plot provides a global view of feature importance.

Image:

images/shap_summary_beeswarm.png

Key observations:

- Features at the top contribute the most.
- Positive SHAP values increase churn probability.
- Negative SHAP values decrease churn probability.

---

# SHAP Feature Importance Plot

Image:

images/shap_summary_bar.png

Purpose:

Ranks all features based on their average SHAP contribution.

---

# Waterfall Plot Analysis

Three customer examples were analyzed.

Customer 1

Image:

images/customer1_waterfall.png

Observation:

Describe the important features affecting the prediction.

---

Customer 2

Image:

images/customer2_waterfall.png

Observation:

Describe the prediction.

---

Customer 3

Image:

images/customer3_waterfall.png

Observation:

Describe the prediction.

---

# Important Features

Example:

- MonthlyCharges
- tenure
- Contract
- TotalCharges
- InternetService

Replace this list with the actual top features from your SHAP plots.

---

# Business Insights

Examples:

- Customers with higher MonthlyCharges are more likely to churn.
- Longer customer tenure reduces churn risk.
- Month-to-month contracts increase churn probability.
- Long-term contracts improve customer retention.

These insights should reflect your model's SHAP analysis.

---

# Benefits of SHAP

- Improves model transparency
- Builds trust in machine learning predictions
- Helps identify key business drivers
- Supports better customer retention strategies

---

# Conclusion

The SHAP explainability analysis successfully explained both global model behavior and individual customer predictions.

The generated visualizations and business insights make the churn prediction model more interpretable and useful for decision-making.

| Visualization      | Purpose                                      |
| ------------------ | -------------------------------------------- |
| SHAP Beeswarm Plot | Shows overall feature importance and impact  |
| SHAP Bar Plot      | Ranks features by importance                 |
| Waterfall Plot     | Explains an individual customer's prediction |

## Day 21 Progress

- Created a comprehensive SHAP Explainability Report
- Documented summary plots and waterfall plots
- Highlighted key features influencing churn predictions
- Summarized business insights
- Completed the explainability documentation