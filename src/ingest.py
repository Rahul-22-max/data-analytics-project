import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.customer import Customer

DATABASE_URL = "sqlite:///telco_churn.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "raw", "Telco-Customer-Churn.csv")

def load_data():
    df = pd.read_csv(csv_path)

    session = Session()

    for _, row in df.iterrows():
        customer = Customer(
            customerID=row["customerID"],
            gender=row["gender"],
            SeniorCitizen=int(row["SeniorCitizen"]),
            Partner=row["Partner"],
            Dependents=row["Dependents"],
            tenure=int(row["tenure"]),
            PhoneService=row["PhoneService"],
            MultipleLines=row["MultipleLines"],
            InternetService=row["InternetService"],
            OnlineSecurity=row["OnlineSecurity"],
            OnlineBackup=row["OnlineBackup"],
            DeviceProtection=row["DeviceProtection"],
            TechSupport=row["TechSupport"],
            StreamingTV=row["StreamingTV"],
            StreamingMovies=row["StreamingMovies"],
            Contract=row["Contract"],
            PaperlessBilling=row["PaperlessBilling"],
            PaymentMethod=row["PaymentMethod"],
            MonthlyCharges=float(row["MonthlyCharges"]),
            TotalCharges=float(row["TotalCharges"]) if str(row["TotalCharges"]).strip() else 0.0,
            Churn=row["Churn"]
        )

        session.add(customer)

    session.commit()
    session.close()

    print(f"{len(df)} records loaded successfully!")


if __name__ == "__main__":
    load_data()