import pandas as pd
import joblib

df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)

X = df.drop("Churn", axis=1)

X = pd.get_dummies(X, drop_first=True)

joblib.dump(
    X.columns.tolist(),
    "saved_models/model_columns.pkl"
)

print("Columns Saved Successfully!")