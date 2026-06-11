import pandas as pd

# Load dataset
df = pd.read_csv("Data/raw/Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing values
df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# Create Tenure Group
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 72],
    labels=[
        "0-1 Year",
        "1-2 Years",
        "2-4 Years",
        "4-6 Years"
    ]
)

# Encode gender
df["gender"] = df["gender"].map({
    "Male": 1,
    "Female": 0
})

# Encode churn
df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

print("Feature Engineering Completed")
print(df.head())

import os

os.makedirs("Data/processed", exist_ok=True)

df.to_csv(
    "Data/processed/cleaned_telco_customer_churn.csv",
    index=False
)

print("Processed dataset saved successfully")