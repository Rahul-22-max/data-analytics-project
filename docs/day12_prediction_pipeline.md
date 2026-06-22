# Day 12 - Prediction Pipeline Report

## Project

**Customer Churn Prediction & Customer Lifetime Value (LTV) Engine**

---

## Objective

The objective of Day 12 was to build a **Prediction Pipeline** using the saved Decision Tree model. The pipeline loads the trained model, prepares customer data, predicts churn, and displays the prediction result.

---

## Dataset Information

* Dataset Name: `cleaned_telco_customer_churn.csv`
* Total Records: **7043**
* Total Features Before Encoding: **31**
* Total Features After Encoding: **33**
* Target Variable: **Churn**
* Saved Model: `churn_prediction_model.pkl`

---

## Prediction Pipeline Workflow

### Step 1: Load Saved Model

The trained Decision Tree model was loaded using the `joblib` library.

```python
model = joblib.load(
    "saved_models/churn_prediction_model.pkl"
)
```

---

### Step 2: Load Processed Dataset

The processed Telco Customer Churn dataset was loaded.

```python
df = pd.read_csv(
    "Data/processed/cleaned_telco_customer_churn.csv"
)
```

---

### Step 3: Prepare Features

* Removed the target column (`Churn`)
* Applied one-hot encoding to categorical features
* Ensured feature dimensions matched the training data

```python
X = df.drop("Churn", axis=1)

X = pd.get_dummies(
    X,
    drop_first=True
)
```

---

### Step 4: Select Sample Customer

A sample customer record was selected from the dataset for testing.

```python
sample_customer = X.iloc[[0]]
```

---

### Step 5: Predict Churn

The trained model predicted whether the selected customer would churn.

```python
prediction = model.predict(
    sample_customer
)
```

---

## Sample Prediction Result

### Model Output

```text
Model Loaded Successfully!

Dataset Shape: (7043, 32)

Features Shape: (7043, 33)

Prediction:
Customer is likely to CHURN

Day 12 Prediction Pipeline Completed!
```

---

## Business Importance

### 1. Real-Time Predictions

The prediction pipeline enables businesses to predict customer churn instantly using customer information.

### 2. Customer Retention

Customers predicted to churn can be targeted with special offers, discounts, or support services to improve retention.

### 3. API Readiness

The prediction pipeline is the foundation for deploying the model through an API, enabling integration with web applications and dashboards.

### 4. Decision Support

Business teams can use churn predictions to make proactive decisions and reduce revenue loss.

---

## Key Results

* Saved model loaded successfully.
* Processed dataset loaded successfully.
* Feature encoding matched training features.
* Prediction pipeline executed without errors.
* Sample customer was predicted as **likely to churn**.
* Pipeline is ready for API deployment.

---

## Day 12 Achievements

✅ Created `predict.py`
✅ Loaded saved Decision Tree model
✅ Prepared customer features for prediction
✅ Generated churn prediction successfully
✅ Tested pipeline with sample customer data
✅ Completed end-to-end prediction workflow
✅ Prepared model for API integration

---

## Conclusion

The Prediction Pipeline was successfully implemented using the saved Decision Tree model.

The model can now:

* Load trained weights
* Accept customer data
* Predict churn status
* Support deployment through APIs and business applications

This marks the completion of the machine learning prediction workflow and prepares the project for deployment.

---

## Next Steps (Day 13)

* Build API using Flask or FastAPI
* Create `/predict` endpoint
* Create `/health` endpoint
* Accept customer data as JSON
* Return churn predictions through API
* Test API using Postman

---

**Prepared By:**
**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 12
