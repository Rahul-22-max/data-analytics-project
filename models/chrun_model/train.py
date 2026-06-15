import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from evaluate import evaluate

# Load dataset
df = pd.read_csv("Data/processed/cleaned_telco_customer_churn.csv")

# Remove non-numeric column if present
if "TenureGroup" in df.columns:
    df = df.drop("TenureGroup", axis=1)

# Features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
evaluate(y_test, y_pred)

print("Logistic Regression Model Trained Successfully")