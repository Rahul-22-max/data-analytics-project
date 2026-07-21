import pandas as pd
import joblib

# Load model
model = joblib.load(
    "models/chrun_model/churn_model.pkl"
)

# Load dataset
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv",
    sep="\t"
)

# Remove target column
X = df.drop("Churn", axis=1)

# Remove non-numeric column
if "TenureGroup" in X.columns:
    X = X.drop("TenureGroup", axis=1)

# Generate predictions
predictions = model.predict(X)
probabilities = model.predict_proba(X)[:, 1]

results = X.copy()
results["Predicted_Churn"] = predictions
results["Churn_Probability"] = probabilities

# Save predictions
results.to_csv(
    "Data/processed/churn_predictions.csv",
    index=False
)

print("Batch prediction completed")
print("Predictions saved to churn_predictions.csv")