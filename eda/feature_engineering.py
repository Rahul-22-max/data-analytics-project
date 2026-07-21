import pandas as pd
import os

# Load dataset
df = pd.read_csv("Data/raw/Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing values with median
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

# Encode Gender
df["gender"] = df["gender"].map({
    "Male": 1,
    "Female": 0
})

# Encode Churn
df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

# Remove customerID because it is unique for every customer
df.drop("customerID", axis=1, inplace=True)

# Find remaining categorical columns
categorical_cols = df.select_dtypes(
    include=["object", "string"]
).columns

print("\nRemaining Categorical Columns:")
print(categorical_cols)

# One-Hot Encode remaining categorical columns
df = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

print("\nAfter Encoding:")
print(df.head())

print("\nFeature Engineering Completed")

# Create processed folder if it doesn't exist
os.makedirs("Data/processed", exist_ok=True)

# Save processed dataset
df.to_csv(
    "Data/processed/cleaned_telco_customer_churn.csv",
    index=False
)

print("\nProcessed dataset saved successfully")
print("Shape of processed dataset:", df.shape)