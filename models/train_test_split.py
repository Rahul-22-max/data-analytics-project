import pandas as pd
from sklearn.model_selection import train_test_split

# Load processed dataset
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)

print("Dataset Shape:", df.shape)

# -----------------------------
# Features and Target
# -----------------------------

X = df.drop("Churn", axis=1)

y = df["Churn"]

print("\nFeatures Shape:", X.shape)

print("Target Shape:", y.shape)

# -----------------------------
# Convert categorical columns
# -----------------------------

X = pd.get_dummies(
    X,
    drop_first=True
)

print("\nAfter Encoding:")

print("Features Shape:", X.shape)

# -----------------------------
# Train-Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Set:")

print(X_train.shape)

print(y_train.shape)

print("\nTesting Set:")

print(X_test.shape)

print(y_test.shape)

print("\nDay 7 Train-Test Split Completed!")