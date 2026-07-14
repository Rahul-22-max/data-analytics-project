import pandas as pd
from utils.model_loader import load_ltv_model

model = load_ltv_model()

def predict_ltv(customer_data):
    try:

        input_df = pd.DataFrame([customer_data])

        prediction = model.predict(input_df)

        return {
            "success": True,
            "predicted_ltv": float(prediction[0])
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }