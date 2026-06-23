from flask import Flask, jsonify
import joblib
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load saved model
model = joblib.load(
    "saved_models/churn_prediction_model.pkl"
)

print("Model Loaded Successfully!")


# Health Check API
@app.route("/health")
def health():

    return jsonify({
        "status": "API Running Successfully"
    })


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    # Load dataset
    df = pd.read_csv(
        "Data/processed/cleaned_telco_customer_churn.csv"
    )

    # Prepare features
    X = df.drop(
        "Churn",
        axis=1
    )

    # One-hot encoding
    X = pd.get_dummies(
        X,
        drop_first=True
    )

    # Take sample customer
    sample_customer = X.iloc[[0]]

    # Make prediction
    prediction = model.predict(
        sample_customer
    )

    # Check result
    if prediction[0] == 1:
        result = "Customer is likely to CHURN"
    else:
        result = "Customer is likely to STAY"

    return jsonify({
        "prediction": result
    })


# Run app
if __name__ == "__main__":
    app.run(debug=True)