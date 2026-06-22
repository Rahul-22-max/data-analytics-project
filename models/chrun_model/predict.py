import joblib
import pandas as pd

# Load saved model
model = joblib.load(
    "models/chrun_model/churn_model.pkl"
)

# Example customer
sample_customer = {
    "gender": 1,
    "SeniorCitizen": 0,
    "tenure": 12,
    "MonthlyCharges": 70,
    "TotalCharges": 840,
    "Partner_Yes": 1,
    "Dependents_Yes": 0,
    "PhoneService_Yes": 1,
    "MultipleLines_No phone service": 0,
    "MultipleLines_Yes": 0,
    "InternetService_Fiber optic": 1,
    "InternetService_No": 0,
    "OnlineSecurity_No internet service": 0,
    "OnlineSecurity_Yes": 1,
    "OnlineBackup_No internet service": 0,
    "OnlineBackup_Yes": 1,
    "DeviceProtection_No internet service": 0,
    "DeviceProtection_Yes": 1,
    "TechSupport_No internet service": 0,
    "TechSupport_Yes": 1,
    "StreamingTV_No internet service": 0,
    "StreamingTV_Yes": 1,
    "StreamingMovies_No internet service": 0,
    "StreamingMovies_Yes": 1,
    "Contract_One year": 1,
    "Contract_Two year": 0,
    "PaperlessBilling_Yes": 1,
    "PaymentMethod_Credit card (automatic)": 1,
    "PaymentMethod_Electronic check": 0,
    "PaymentMethod_Mailed check": 0
}

customer_df = pd.DataFrame([sample_customer])

prediction = model.predict(customer_df)
probability = model.predict_proba(customer_df)

print("Prediction:", prediction[0])
print("Churn Probability:", probability[0][1])