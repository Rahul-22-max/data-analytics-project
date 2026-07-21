# Day 6 Feature Selection Report

## Objective

Identify the most important features affecting customer churn and prepare the dataset for Machine Learning modeling.

---

## Top Positive Correlations with Churn

| Feature                        | Correlation |
| ------------------------------ | ----------: |
| InternetService_Fiber optic    |       0.308 |
| PaymentMethod_Electronic check |       0.302 |
| MonthlyCharges                 |       0.193 |
| PaperlessBilling_Yes           |       0.192 |
| SeniorCitizen                  |       0.151 |

### Interpretation

These features increase the likelihood of customer churn.

* Fiber optic customers show the highest churn tendency.
* Customers using Electronic Check are more likely to leave.
* Higher monthly charges are associated with increased churn.

---

## Top Negative Correlations with Churn

| Feature            | Correlation |
| ------------------ | ----------: |
| tenure             |      -0.352 |
| Contract_Two year  |      -0.302 |
| OnlineSecurity_Yes |      -0.171 |
| TechSupport_Yes    |      -0.165 |
| Partner_Yes        |      -0.150 |

### Interpretation

These features reduce the likelihood of customer churn.

* Long-term customers are more loyal.
* Customers with Two-Year contracts churn much less.
* Security and support services improve customer retention.

---

## Features Selected for Machine Learning

Selected features:

* tenure
* MonthlyCharges
* TotalCharges
* SeniorCitizen
* InternetService_Fiber optic
* Contract_One year
* Contract_Two year
* PaymentMethod_Electronic check
* OnlineSecurity_Yes
* TechSupport_Yes
* PaperlessBilling_Yes
* Partner_Yes
* Dependents_Yes

---

## Conclusion

The correlation analysis and visualization identified the most important factors influencing customer churn. These features will be used by Member 3 for churn prediction model development.

---

**Prepared By:**
B. Rahul Charan Babu
Team Lead & Member 2

**Project Day:** 6
