import pandas as pd
import matplotlib.pyplot as plt

# Load processed dataset
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)

# Calculate correlation with Churn
correlation = df.corr(numeric_only=True)

churn_corr = (
    correlation["Churn"]
    .drop("Churn")
    .sort_values()
)

print("\nCorrelation with Churn:")
print(churn_corr)

# Plot correlation bar chart
churn_corr.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Feature Correlation with Churn")
plt.xlabel("Features")
plt.ylabel("Correlation")

plt.xticks(rotation=90)

plt.tight_layout()

plt.show()

print("\nDay 6 Correlation Visualization Completed!")