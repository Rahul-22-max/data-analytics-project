# Day 14 - Flask Prediction API Development

## Project

**Customer Churn Prediction & Customer Lifetime Value (LTV) Engine**

---

## Objective

The objective of Day 14 was to develop a Flask-based REST API that loads the trained churn prediction model and provides churn predictions through HTTP endpoints.

---

## Tasks Completed

### 1. Flask API Setup

* Installed and configured Flask.
* Created `api/app.py`.
* Configured Flask application structure.

---

### 2. Model Integration

* Loaded saved Decision Tree model:

  `saved_models/churn_prediction_model.pkl`

* Loaded saved feature columns:

  `saved_models/model_columns.pkl`

* Verified successful model loading during API startup.

---

### 3. Health Check Endpoint

Created a health endpoint:

```http
GET /health
```

Response:

```json
{
    "status": "API Running Successfully"
}
```

Purpose:

* Verify API availability.
* Confirm server is running correctly.

---

### 4. Prediction Endpoint

Created prediction endpoint:

```http
POST /predict
```

Functionality:

* Accepts customer data in JSON format.
* Converts JSON input into a Pandas DataFrame.
* Applies one-hot encoding.
* Aligns incoming data with training feature columns.
* Uses the saved Decision Tree model for prediction.
* Returns prediction as JSON.

---

## Sample Request

```json
{
    "gender": 0,
    "SeniorCitizen": 0,
    "tenure": 1,
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85
}
```

---

## Sample Response

```json
{
    "prediction": "Customer is likely to CHURN"
}
```

---

## API Testing

### Browser Testing

Endpoint:

```http
http://127.0.0.1:5000/health
```

Result:

* API responded successfully.
* Health status verified.

### Postman Testing

Endpoint:

```http
POST http://127.0.0.1:5000/predict
```

Result:

* JSON request processed successfully.
* Prediction returned correctly.
* API functioning as expected.

---

## Technical Components Used

| Component              | Technology               |
| ---------------------- | ------------------------ |
| API Framework          | Flask                    |
| Machine Learning Model | Decision Tree Classifier |
| Model Storage          | Joblib                   |
| Data Processing        | Pandas                   |
| API Testing            | Postman                  |

---

## Business Value

### 1. Real-Time Predictions

The API allows customer churn predictions to be generated in real time.

### 2. Deployment Readiness

The machine learning model is now accessible through a REST API, making integration with dashboards and business applications easier.

### 3. Scalable Architecture

The API layer separates prediction logic from the user interface, supporting future deployment and scaling.

---

## Conclusion

Day 14 successfully transformed the trained Decision Tree model into a working prediction service using Flask.

The API can now:

* Load the saved model.
* Accept customer data.
* Generate churn predictions.
* Return results through JSON responses.

This completes the machine learning serving layer of the project.

---

## Day 14 Achievements

✅ Created Flask API

✅ Created `/health` endpoint

✅ Created `/predict` endpoint

✅ Loaded saved Decision Tree model

✅ Loaded saved training columns

✅ Accepted customer data as JSON

✅ Generated churn predictions

✅ Tested API using Postman

✅ Verified successful API responses

✅ Generated `day14_api_prediction.md`

---

## Next Steps (Day 15)

* Final project documentation
* Update README with API usage guide
* Project cleanup and validation
* Team report finalization
* Deployment preparation
* Final project submission

---

**Prepared By:**

**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 14
