import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/raw/Telco-Customer-Churn.csv")

# Contract vs Churn
pd.crosstab(df["Contract"], df["Churn"]).plot(kind="bar")

plt.title("Contract Type vs Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.show()

# Internet Service vs Churn
pd.crosstab(df["InternetService"], df["Churn"]).plot(kind="bar")

plt.title("Internet Service vs Churn")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Payment Method vs Churn
pd.crosstab(df["PaymentMethod"], df["Churn"]).plot(kind="bar")

plt.title("Payment Method vs Churn")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()