import pandas as pd
import joblib

# ---------------------------------

# Load Saved Model

# ---------------------------------

model = joblib.load(
"saved_models/churn_prediction_model.pkl"
)

print("Model Loaded Successfully!")

# ---------------------------------

# Load Dataset

# ---------------------------------

df = pd.read_csv(
"Data/processed/cleaned_telco_customer_churn.csv"
)

print("\nDataset Shape:", df.shape)

# ---------------------------------

# Prepare Features

# ---------------------------------

X = df.drop("Churn", axis=1)

# One-hot encoding

X = pd.get_dummies(X, drop_first=True)

print("\nFeatures Shape:", X.shape)

print("\nFeature Names:")

for col in X.columns:
    print(col)

# ---------------------------------

# Take a Sample Customer

# ---------------------------------

sample_customer = X.iloc[[0]]

print("\nSample Customer Data:")

print(sample_customer)

# ---------------------------------

# Predict

# ---------------------------------

prediction = model.predict(sample_customer)

print("\nPrediction:")

if prediction[0] == 1:
    print("Customer is likely to CHURN")
else:
    print("Customer is likely to STAY")

# ---------------------------------

# Completion Message

# ---------------------------------

print("\nDay 12 Prediction Pipeline Completed!")
