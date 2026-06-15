import pandas as pd

# Load processed dataset
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)

print("Dataset Shape:", df.shape)

# Calculate correlation matrix
correlation = df.corr(numeric_only=True)

# Correlation with Churn
churn_corr = correlation["Churn"].sort_values(
    ascending=False
)

print("\n===== CORRELATION WITH CHURN =====")

print(churn_corr)

# Remove Churn itself from the list
churn_corr = churn_corr.drop("Churn")

# ---------------------------------
# Top Positive Correlations
# ---------------------------------

print("\nTop 10 Features Affecting Churn:")

print(
    churn_corr.head(10)
)

# ---------------------------------
# Top Negative Correlations
# ---------------------------------

print("\nTop 10 Features Negatively Correlated with Churn:")

print(
    churn_corr.tail(10)
)

print("\nDay 5 Correlation Analysis Completed!")