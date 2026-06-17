import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv",
    sep="\t"
)

if "TenureGroup" in df.columns:
    df = df.drop("TenureGroup", axis=1)

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

print("Logistic Regression Accuracy:",
      accuracy_score(y_test, lr.predict(X_test)))

print("Decision Tree Accuracy:",
      accuracy_score(y_test, dt.predict(X_test)))