import pandas as pd
import joblib
from evaluate import evaluate
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv",
    sep="\t"
)

# Remove columns that contain text values
if "TenureGroup" in df.columns:
    df = df.drop("TenureGroup", axis=1)

# Features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Logistic Regression Model
model = LogisticRegression(
    max_iter=2000,
    solver="liblinear"
)

model.fit(X_train, y_train)

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

# Save model
joblib.dump(
    model,
    "models/chrun_model/churn_model.pkl"
)

print("Model saved successfully")

# Predictions
y_pred = model.predict(X_test)

# ROC-AUC Score
from sklearn.metrics import roc_auc_score

y_prob = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, y_prob)

print(f"\nROC-AUC Score: {auc:.4f}")


# Evaluation
evaluate(y_test, y_pred)

from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

print("Logistic Regression Model Trained Successfully")