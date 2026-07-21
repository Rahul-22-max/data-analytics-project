import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv",
    sep="\t"
)

if "TenureGroup" in df.columns:
    df = df.drop("TenureGroup", axis=1)

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = LogisticRegression(
    max_iter=2000,
    solver="liblinear"
)

model.fit(X_train, y_train)

importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

importance["Abs_Coefficient"] = importance["Coefficient"].abs()

importance = importance.sort_values(
    by="Abs_Coefficient",
    ascending=False
)

print("\nTop 10 Important Features:")
print(
    importance[
        ["Feature", "Coefficient", "Abs_Coefficient"]
    ].head(10)
)