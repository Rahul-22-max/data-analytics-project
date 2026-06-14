import pandas as pd
import matplotlib.pyplot as plt

# Load processed dataset
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)

# ---------------------------------
# Churn Distribution
# ---------------------------------

df["Churn"].value_counts().plot(kind="bar")

plt.title("Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# ---------------------------------
# Churn Rate by Gender
# ---------------------------------

gender_churn = df.groupby("gender")["Churn"].mean()

gender_churn.plot(kind="bar")

plt.title("Churn Rate by Gender")
plt.xlabel("Gender (0=Female, 1=Male)")
plt.ylabel("Churn Rate")

plt.tight_layout()
plt.show()

# ---------------------------------
# Churn Rate by Contract
# ---------------------------------

contract_cols = [
    col
    for col in df.columns
    if "Contract_" in col
]

for col in contract_cols:

    churn_rate = df.groupby(col)["Churn"].mean()

    churn_rate.plot(kind="bar")

    plt.title(f"Churn Rate - {col}")
    plt.xlabel(col)
    plt.ylabel("Churn Rate")

    plt.tight_layout()
    plt.show()

# ---------------------------------
# Churn Rate by Tenure Group
# ---------------------------------

tenure_churn = df.groupby(
    "TenureGroup"
)["Churn"].mean()

tenure_churn.plot(kind="bar")

plt.title("Churn Rate by Tenure Group")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate")

plt.tight_layout()
plt.show()

print("\nDay 4 Visualization Completed!")