import pandas as pd

df = pd.read_csv("Data/processed/cleaned_telco_customer_churn.csv")

print("\n===== CHURN DISTRIBUTION =====")
print(df["Churn"].value_counts())

print("\n===== CHURN BY CONTRACT =====")
print(pd.crosstab(df["Contract"], df["Churn"]))

print("\n===== CHURN BY TENURE GROUP =====")
print(pd.crosstab(df["TenureGroup"], df["Churn"]))

print("\n===== CHURN BY PAYMENT METHOD =====")
print(pd.crosstab(df["PaymentMethod"], df["Churn"]))