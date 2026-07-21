import pandas as pd


def preprocess_input(data):
    """
    Convert API request into a DataFrame
    compatible with the ML model.
    """

    df = pd.DataFrame([{
        "tenure": data.tenure,
        "MonthlyCharges": data.monthly_charges,
        "Contract": data.contract
    }])

    return df