# Telco Customer Churn Dataset - Data Dictionary

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| customerID | String | Unique customer identifier |
| gender | String | Customer gender (Male/Female) |
| SeniorCitizen | Integer | Whether customer is a senior citizen (1 = Yes, 0 = No) |
| Partner | String | Whether customer has a partner |
| Dependents | String | Whether customer has dependents |
| tenure | Integer | Number of months customer has stayed with the company |
| PhoneService | String | Whether customer has phone service |
| MultipleLines | String | Whether customer has multiple phone lines |
| InternetService | String | Type of internet service |
| OnlineSecurity | String | Whether customer has online security service |
| OnlineBackup | String | Whether customer has online backup service |
| DeviceProtection | String | Whether customer has device protection |
| TechSupport | String | Whether customer has technical support |
| StreamingTV | String | Whether customer has streaming TV |
| StreamingMovies | String | Whether customer has streaming movie service |
| Contract | String | Customer contract type |
| PaperlessBilling | String | Whether customer uses paperless billing |
| PaymentMethod | String | Customer payment method |
| MonthlyCharges | Float | Monthly bill amount |
| TotalCharges | Float | Total amount charged to the customer |
| Churn | String | Whether customer left the company (Yes/No) |

## Target Table

**Table Name:** `customers`

## Primary Key

- `customerID`

## Data Source

- Telco Customer Churn Dataset

## Created By

- Data Engineering Team
S.MOHAMED JAVEETH