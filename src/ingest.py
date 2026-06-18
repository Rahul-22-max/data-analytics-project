import pandas as pd

def load_data():
    file_path = "Data/raw/Telco-Customer-Churn.csv"

    df = pd.read_csv(file_path)

    return df

if __name__ == "__main__":
    df = load_data()

    print(df.head())