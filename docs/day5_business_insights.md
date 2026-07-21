# Day 5 Business Insights

## Correlation Analysis Summary

The correlation analysis was performed to identify the factors that have the strongest relationship with customer churn.

---

## Top Features Increasing Churn

| Feature                        | Correlation |
| ------------------------------ | ----------: |
| InternetService_Fiber optic    |       0.308 |
| PaymentMethod_Electronic check |       0.302 |
| MonthlyCharges                 |       0.193 |
| PaperlessBilling_Yes           |       0.192 |
| SeniorCitizen                  |       0.151 |

### Insights

* Customers using **Fiber Optic Internet Service** are more likely to churn.
* Customers paying through **Electronic Check** have a higher probability of leaving.
* Higher **Monthly Charges** are associated with increased churn.
* Senior citizens show a slightly higher churn tendency.

---

## Top Features Reducing Churn

| Feature                         | Correlation |
| ------------------------------- | ----------: |
| tenure                          |      -0.352 |
| Contract_Two year               |      -0.302 |
| InternetService_No              |      -0.228 |
| TechSupport_No internet service |      -0.228 |
| TotalCharges                    |      -0.199 |

### Insights

* Customers with **longer tenure** are less likely to churn.
* Customers having a **Two-Year Contract** are more loyal.
* Customers who stay longer with the company contribute to higher total charges and lower churn rates.

---

## Business Recommendations

1. Offer attractive long-term contract plans to customers.
2. Investigate why Fiber Optic customers are leaving and improve service quality.
3. Provide incentives to customers using Electronic Check to reduce churn.
4. Focus retention campaigns on new customers because churn is highest during the early tenure period.
5. Introduce loyalty rewards for long-term customers.

---

## Conclusion

The correlation analysis shows that **contract duration**, **customer tenure**, **internet service type**, and **payment method** are the most important factors influencing customer churn.

Understanding these relationships can help businesses design better retention strategies and improve customer satisfaction.

---

**Prepared By:**
B. Rahul Charan Babu
Team Lead & Member 2

**Project Day:** 5
