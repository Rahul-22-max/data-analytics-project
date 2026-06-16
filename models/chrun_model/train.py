import pandas as pd
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

# Check for any remaining text columns
print("Object columns:")
print(df.select_dtypes(include=["object"]).columns.tolist())

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
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
evaluate(y_test, y_pred)

print("Logistic Regression Model Trained Successfully")