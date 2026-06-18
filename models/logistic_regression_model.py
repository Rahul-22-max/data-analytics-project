import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# ---------------------------------
# Load Dataset
# ---------------------------------

df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)

print("Dataset Shape:", df.shape)

# ---------------------------------
# Features and Target
# ---------------------------------

X = df.drop("Churn", axis=1)

y = df["Churn"]

# Convert categorical columns

X = pd.get_dummies(
    X,
    drop_first=True
)

print("\nFeatures Shape:", X.shape)

print("Target Shape:", y.shape)

# ---------------------------------
# Train-Test Split
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Shape:")

print(X_train.shape)

print(y_train.shape)

print("\nTesting Shape:")

print(X_test.shape)

print(y_test.shape)

# ---------------------------------
# Train Logistic Regression Model
# ---------------------------------

model = LogisticRegression(
    solver="liblinear",
    max_iter=2000,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

print("\nModel Training Completed!")

# ---------------------------------
# Prediction
# ---------------------------------

y_pred = model.predict(X_test)

# ---------------------------------
# Evaluation
# ---------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n===== ACCURACY =====")

print(f"{accuracy:.4f}")

print("\n===== CONFUSION MATRIX =====")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

print("\n===== CLASSIFICATION REPORT =====")

print(
    classification_report(
        y_test,
        y_pred
    )
)

print("\nDay 8 Logistic Regression Completed!")