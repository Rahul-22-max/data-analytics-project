import pandas as pd

# Load processed dataset
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)

print("Dataset Shape:", df.shape)

# ---------------------------------
# Churn Distribution
# ---------------------------------

print("\n===== CHURN DISTRIBUTION =====")

print(df["Churn"].value_counts())

# ---------------------------------
# Churn Rate by Gender
# ---------------------------------

print("\n===== CHURN RATE BY GENDER =====")

print(
    df.groupby("gender")["Churn"].mean()
)

# ---------------------------------
# Churn Rate by Contract
# ---------------------------------

print("\n===== CHURN RATE BY CONTRACT =====")

contract_cols = [
    col
    for col in df.columns
    if "Contract_" in col
]

for col in contract_cols:

    print(f"\n{col}")

    print(
        df.groupby(col)["Churn"].mean()
    )

# ---------------------------------
# Churn Rate by Tenure Group
# ---------------------------------

print("\n===== CHTURN RATE BY TENURE GROUP =====")

print(
    df.groupby("TenureGroup")["Churn"].mean()
)

# ---------------------------------
# Show All Columns
# ---------------------------------

print("\n===== ALL COLUMNS =====")

print(df.columns)

print("\nDay 4 Churn Analysis Completed!")