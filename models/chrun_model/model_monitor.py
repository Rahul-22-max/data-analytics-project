import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

# -----------------------------
# Load Dataset
# -----------------------------
DATA_PATH = "Data/processed/cleaned_telco_customer_churn.csv"

df = pd.read_csv(DATA_PATH, sep="\t")

# Remove non-numeric column if present
if "TenureGroup" in df.columns:
    df = df.drop("TenureGroup", axis=1)

X = df.drop("Churn", axis=1)
y = df["Churn"]

# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# Load Saved Model
# -----------------------------
MODEL_PATH = "models/chrun_model/churn_model.pkl"

model = joblib.load(MODEL_PATH)

# -----------------------------
# Predictions
# -----------------------------
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# -----------------------------
# Metrics
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# -----------------------------
# Print Results
# -----------------------------
print("\n===== Model Performance =====")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC AUC  : {roc_auc:.4f}")

print("\nConfusion Matrix")
print(f"TN: {tn}")
print(f"FP: {fp}")
print(f"FN: {fn}")
print(f"TP: {tp}")

# -----------------------------
# Save Report
# -----------------------------
os.makedirs("reports", exist_ok=True)

with open("reports/model_performance_report.md", "w") as report:

    report.write("# Model Performance Report\n\n")
    report.write("## Model\n")
    report.write("Logistic Regression\n\n")

    report.write("## Evaluation Metrics\n\n")
    report.write(f"- Accuracy: {accuracy:.4f}\n")
    report.write(f"- Precision: {precision:.4f}\n")
    report.write(f"- Recall: {recall:.4f}\n")
    report.write(f"- F1 Score: {f1:.4f}\n")
    report.write(f"- ROC-AUC Score: {roc_auc:.4f}\n\n")

    report.write("## Confusion Matrix\n\n")
    report.write(f"- True Negatives : {tn}\n")
    report.write(f"- False Positives: {fp}\n")
    report.write(f"- False Negatives: {fn}\n")
    report.write(f"- True Positives : {tp}\n")

print("\nReport saved to reports/model_performance_report.md")

# -----------------------------
# Save Metrics CSV
# -----------------------------
metrics = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"
    ],
    "Value": [
        accuracy,
        precision,
        recall,
        f1,
        roc_auc
    ]
})

metrics.to_csv("reports/model_metrics.csv", index=False)

print("Metrics saved to reports/model_metrics.csv")