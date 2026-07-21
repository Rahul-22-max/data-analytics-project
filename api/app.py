from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load Model
model = joblib.load("saved_models/churn_prediction_model.pkl")

# Load Training Columns
model_columns = joblib.load("saved_models/model_columns.pkl")

print("Model Loaded Successfully!")

# Health Endpoint
@app.route("/health")
def health():
    return jsonify({
        "status": "API Running Successfully"
    })

# Prediction Endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    # Convert incoming JSON dict to DataFrame
    df = pd.DataFrame([data])
    
    # One-hot encoding
    df = pd.get_dummies(df)
    
    # Align columns: adds missing columns as 0 and discards extra columns
    df = df.reindex(columns=model_columns, fill_value=0)
    
    # Make prediction
    prediction = model.predict(df)
    
    if prediction[0] == 1:
        result = "Customer is likely to CHURN"
    else:
        result = "Customer is likely to STAY"
        
    return jsonify({
        "prediction": result
    })

# Run Flask
if __name__ == "__main__":
    app.run(debug=True)