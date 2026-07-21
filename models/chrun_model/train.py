import os
import sys

# ==========================================================
# Add Project Root to Python Path
# ==========================================================
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
import joblib

from evaluate import evaluate
from model_versioning import save_model_version
from data_loader import load_data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

# ==========================================================
# Import Configuration
# ==========================================================
from config.config import (
    DATA_PATH,
    MODEL_PATH,
    REPORTS_DIR,
    TEST_SIZE,
    RANDOM_STATE,
    MAX_ITER,
    SOLVER
)

# ==========================================================
# Create Required Directories
# ==========================================================
os.makedirs(REPORTS_DIR, exist_ok=True)

# ==========================================================
# Load Dataset
# ==========================================================
df = load_data(DATA_PATH)

# Remove non-numeric column if present
if "TenureGroup" in df.columns:
    df = df.drop("TenureGroup", axis=1)

# ==========================================================
# Features and Target
# ==========================================================
X = df.drop("Churn", axis=1)
y = df["Churn"]

# ==========================================================
# Train/Test Split
# ==========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y
)

# ==========================================================
# Train Logistic Regression Model
# ==========================================================
model = LogisticRegression(
    max_iter=MAX_ITER,
    solver=SOLVER
)

model.fit(X_train, y_train)

# ==========================================================
# Feature Importance
# ==========================================================
coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

coef_df["Abs_Coefficient"] = coef_df["Coefficient"].abs()

coef_df = coef_df.sort_values(
    by="Abs_Coefficient",
    ascending=False
)

print("\nTop 10 Important Features:")
print(coef_df.head(10))

feature_importance_path = os.path.join(
    REPORTS_DIR,
    "logistic_feature_importance.csv"
)

coef_df.to_csv(
    feature_importance_path,
    index=False
)

print("\nFeature importance saved successfully.")

# ==========================================================
# Predictions
# ==========================================================
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# ==========================================================
# Evaluation Metrics
# ==========================================================
accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_prob)

print(f"\nAccuracy : {accuracy:.4f}")
print(f"ROC-AUC  : {auc:.4f}")

# ==========================================================
# Save Latest Model
# ==========================================================
joblib.dump(model, MODEL_PATH)

print("\nLatest model saved successfully.")

# ==========================================================
# Save Versioned Model
# ==========================================================
save_model_version(
    source_model_path=MODEL_PATH,
    accuracy=accuracy,
    algorithm="Logistic Regression",
    notes="Baseline production model"
)

# ==========================================================
# Evaluation
# ==========================================================
print("\nEvaluation Metrics")
evaluate(y_test, y_pred)

# ==========================================================
# Classification Report
# ==========================================================
report = classification_report(y_test, y_pred)

print("\nClassification Report:")
print(report)

report_path = os.path.join(
    REPORTS_DIR,
    "classification_report.txt"
)

with open(report_path, "w") as file:
    file.write(report)

print("\nClassification report saved successfully.")

# ==========================================================
# Confusion Matrix
# ==========================================================
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

print("\nLogistic Regression Model Trained Successfully")