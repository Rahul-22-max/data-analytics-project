| Column          | Meaning                            |
| --------------- | ---------------------------------- |
| customerID      | Unique customer identifier         |
| gender          | Male/Female                        |
| SeniorCitizen   | Whether customer is senior citizen |
| Partner         | Has partner or not                 |
| Dependents      | Has dependents or not              |
| tenure          | Number of months customer stayed   |
| PhoneService    | Phone service subscription         |
| InternetService | Type of internet service           |
| MonthlyCharges  | Monthly bill amount                |
| TotalCharges    | Total amount paid                  |
| Churn           | Customer left or stayed            |

# Revenue Related Columns

1. tenure
   - Number of months customer has stayed.

2. MonthlyCharges
   - Monthly recurring revenue.

3. TotalCharges
   - Total revenue generated from customer.

These three columns are important for LTV calculation.

LTV = MonthlyCharges × Tenure

LTV = Average Revenue Per User × Customer Lifespan

LTV = MonthlyCharges × Tenure × Retention Probability

LTV =
Average Monthly Revenue
× Expected Remaining Lifetime
× Retention Rate