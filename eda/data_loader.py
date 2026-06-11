import pandas as pd

# Load dataset
df = pd.read_csv("../Data/raw/Telco-Customer-Churn.csv")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check unique values in Churn column
print("\nChurn Value Counts:")
print(df["Churn"].value_counts())

# Check missing values again
print("\nMissing Values:")
print(df.isnull().sum())

# Display data types
print("\nData Types:")
print(df.dtypes)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print("\nTotalCharges Data Type:")
print(df["TotalCharges"].dtype)

print("\nMissing values after conversion:")
print(df["TotalCharges"].isnull().sum())

import matplotlib.pyplot as plt

# Churn distribution
df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()

print("\nContract vs Churn:")
print(pd.crosstab(df["Contract"], df["Churn"]))

print("\nInternet Service vs Churn:")
print(pd.crosstab(df["InternetService"], df["Churn"]))

print("\nPayment Method vs Churn:")
print(pd.crosstab(df["PaymentMethod"], df["Churn"]))

print("\nAverage Tenure by Churn:")
print(df.groupby("Churn")["tenure"].mean())