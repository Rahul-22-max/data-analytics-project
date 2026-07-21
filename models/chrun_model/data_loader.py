import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, sep="\t")
    return df

if __name__ == "__main__":
    print("Data loader initialized")