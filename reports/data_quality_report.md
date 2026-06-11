# Data Quality Report

## Dataset Information

- Dataset: Telco Customer Churn
- Rows: 7043
- Columns: 21

## Missing Values

== NULL VALUES ==
customerID          0
gender              0
SeniorCitizen       0
Partner             0
Dependents          0
tenure              0
PhoneService        0
MultipleLines       0
InternetService     0
OnlineSecurity      0
OnlineBackup        0
DeviceProtection    0
TechSupport         0
StreamingTV         0
StreamingMovies     0
Contract            0
PaperlessBilling    0
PaymentMethod       0
MonthlyCharges      0
TotalCharges        0
Churn               0
dtype: int64

 === EMPTY STRINGS ==
customerID           0
gender               0
SeniorCitizen        0
Partner              0
Dependents           0
tenure               0
PhoneService         0
MultipleLines        0
InternetService      0
OnlineSecurity       0
OnlineBackup         0
DeviceProtection     0
TechSupport          0
StreamingTV          0
StreamingMovies      0
Contract             0
PaperlessBilling     0
PaymentMethod        0
MonthlyCharges       0
TotalCharges        11
Churn                0
dtype: int64

 === Summary report ===
                  Null Values  Empty Strings
customerID                  0              0
gender                      0              0
SeniorCitizen               0              0
Partner                     0              0
Dependents                  0              0
tenure                      0              0
PhoneService                0              0
MultipleLines               0              0
InternetService             0              0
OnlineSecurity              0              0
OnlineBackup                0              0
DeviceProtection            0              0
TechSupport                 0              0
StreamingTV                 0              0
StreamingMovies             0              0
Contract                    0              0
PaperlessBilling            0              0
PaymentMethod               0              0
MonthlyCharges              0              0
TotalCharges                0             11
Churn                       0              0

## Duplicate Records

Duplicate Records: 0

## Data Type 

Data Types:
customerID              str
gender                  str
SeniorCitizen         int64
Partner                 str
Dependents              str
tenure                int64
PhoneService            str
MultipleLines           str
InternetService         str
OnlineSecurity          str
OnlineBackup            str
DeviceProtection        str
TechSupport             str
StreamingTV             str
StreamingMovies         str
Contract                str
PaperlessBilling        str
PaymentMethod           str
MonthlyCharges      float64
TotalCharges            str
Churn                   str
dtype: object

## Conclusion

Dataset reviewed and ready for preprocessing.