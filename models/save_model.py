import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset

df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)

print("Dataset Shape:", df.shape)

# Separate features and target

X = df.drop(
    "Churn",
    axis=1
)

y = df["Churn"]

print("\nFeatures Shape:", X.shape)

print("Target Shape:", y.shape)

# One-hot encoding

X = pd.get_dummies(
    X,
    drop_first=True
)

print("\nAfter Encoding:")

print("Features Shape:", X.shape)

# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Shape:")

print(X_train.shape)

print(y_train.shape)

print("\nTesting Shape:")

print(X_test.shape)

print(y_test.shape)

# Train Decision Tree Model

model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

print("\nModel Training Completed!")

# Create folder if it does not exist

os.makedirs(
    "saved_models",
    exist_ok=True
)

# Save model

joblib.dump(
    model,
    "saved_models/churn_prediction_model.pkl"
)

print("\nModel Saved Successfully!")

print("\nLocation:")

print(
    "saved_models/churn_prediction_model.pkl"
)

print("\nDay 11 Model Saving Completed!")