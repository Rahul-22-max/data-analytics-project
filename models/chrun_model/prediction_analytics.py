import pandas as pd

df = pd.read_csv(
    "Data/processed/churn_predictions.csv"
)

total_customers = len(df)

high_risk = len(
    df[df["Churn_Probability"] >= 0.70]
)

medium_risk = len(
    df[
        (df["Churn_Probability"] >= 0.40) &
        (df["Churn_Probability"] < 0.70)
    ]
)

low_risk = len(
    df[df["Churn_Probability"] < 0.40]
)

print("\nCustomer Risk Summary")
print("-" * 30)

print(f"Total Customers : {total_customers}")
print(f"High Risk       : {high_risk}")
print(f"Medium Risk     : {medium_risk}")
print(f"Low Risk        : {low_risk}")

risk_report = pd.DataFrame({
    "Category": [
        "High Risk",
        "Medium Risk",
        "Low Risk"
    ],
    "Customers": [
        high_risk,
        medium_risk,
        low_risk
    ]
})

risk_report.to_csv(
    "Data/processed/risk_summary.csv",
    index=False
)

print("\nRisk summary exported.")