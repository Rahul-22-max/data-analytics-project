from utils.model_loader import load_ltv_model

model = load_ltv_model()

def predict(data):
    prediction = model.predict(data)

    return float(prediction[0])