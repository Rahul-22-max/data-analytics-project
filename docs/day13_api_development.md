# Day 13 - API Development Report

## Project

**Customer Churn Prediction & Customer Lifetime Value (LTV) Engine**

---

## Objective

The objective of Day 13 was to build a Flask API for the Customer Churn Prediction model and prepare the project for deployment.

---

## Tasks Completed

### 1. Installed Flask Framework

* Verified Flask installation using:

```bash
py -m pip show flask
```

* Flask Version:

**3.1.3**

---

### 2. Created API Folder Structure

Created the following structure:

```text
api/
└── app.py

saved_models/
└── churn_prediction_model.pkl

Data/
└── processed/
    └── cleaned_telco_customer_churn.csv
```

---

### 3. Loaded Saved Model

Successfully loaded the trained Decision Tree model using:

```python
model = joblib.load(
    "saved_models/churn_prediction_model.pkl"
)
```

Output:

```text
Model Loaded Successfully!
```

---

### 4. Created Health Check Endpoint

Created a `/health` endpoint to verify API status.

**URL**

```text
http://127.0.0.1:5000/health
```

**Response**

```json
{
    "status": "API Running Successfully"
}
```

---

### 5. Ran Flask Application

Executed:

```bash
py api/app.py
```

Output:

```text
* Running on http://127.0.0.1:5000
```

The API server started successfully in debug mode.

---

## API Endpoints

| Endpoint   | Method | Purpose                                             |
| ---------- | ------ | --------------------------------------------------- |
| `/health`  | GET    | Check API status                                    |
| `/predict` | POST   | Predict customer churn *(to be enhanced in Day 14)* |

---

## Challenges Faced

### Feature Mismatch Error

While testing the `/predict` endpoint using Postman, the following error occurred:

```text
ValueError:
The feature names should match those that were passed during fit.
Feature names seen at fit time, yet now missing:
- Contract_One year
- Contract_Two year
- Dependents_Yes
...
```

### Reason

The model was trained using **33 encoded features**, but Postman requests contained only a few raw features.

Example:

```json
{
    "gender": 0,
    "SeniorCitizen": 0,
    "tenure": 1,
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85
}
```

Therefore, custom prediction requests will be implemented after adding preprocessing logic.

---

## Business Insights

1. Flask API setup was completed successfully.
2. The saved Decision Tree model can be loaded inside the API.
3. Health endpoint verifies server availability.
4. Prediction endpoint structure is ready.
5. Full JSON-based prediction support will be implemented in the next phase.

---

## Conclusion

Day 13 focused on API development and deployment preparation.

The Flask application was created successfully, the saved model was loaded, and the health endpoint was tested successfully.

The project is now ready for implementing a complete prediction API.

---

## Day 13 Achievements

✅ Installed and configured Flask
✅ Created `api/app.py`
✅ Loaded saved Decision Tree model
✅ Created `/health` endpoint
✅ Started Flask server successfully
✅ Prepared `/predict` endpoint structure
✅ Generated `day13_api_development.md`

---

## Next Steps (Day 14)

* Implement full prediction API
* Accept customer data through JSON
* Apply preprocessing automatically
* Match training feature columns
* Return prediction results as JSON
* Test API using Postman

---

**Prepared By:**
**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 13
