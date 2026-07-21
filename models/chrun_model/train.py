import pandas as pd
import joblib

from evaluate import evaluate
from model_versioning import save_model_version

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv",
    sep="\t"
)

# Remove non-numeric column if present
if "TenureGroup" in df.columns:
    df = df.drop("TenureGroup", axis=1)

# -----------------------------
# Features and Target
# -----------------------------
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
# Train Logistic Regression Model
# -----------------------------
model = LogisticRegression(
    max_iter=2000,
    solver="liblinear"
)

model.fit(X_train, y_train)

# -----------------------------
# Feature Importance
# -----------------------------
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

coef_df.to_csv(
    "reports/logistic_feature_importance.csv",
    index=False
)

# -----------------------------
# Predictions
# -----------------------------
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# -----------------------------
# Metrics
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_prob)

print(f"\nROC-AUC Score: {auc:.4f}")

# -----------------------------
# Save Latest Model
# -----------------------------
model_path = "models/chrun_model/churn_model.pkl"

joblib.dump(model, model_path)

print("\nLatest model saved successfully.")

# -----------------------------
# Save Versioned Model
# -----------------------------
save_model_version(
    source_model_path=model_path,
    accuracy=accuracy,
    algorithm="Logistic Regression",
    notes="Baseline production model"
)

# -----------------------------
# Evaluation
# -----------------------------
print("\nEvaluation Metrics")
evaluate(y_test, y_pred)

# -----------------------------
# Classification Report
# -----------------------------
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

print("\nLogistic Regression Model Trained Successfully")

