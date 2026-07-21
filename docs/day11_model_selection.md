# Day 11 - Model Selection and Model Saving Report

## Project

**Customer Churn Prediction & Customer Lifetime Value (LTV) Engine**

---

## Objective

The objective of Day 11 was to compare all trained machine learning models, identify the best performing model, and save the selected model for future deployment and prediction.

---

## Models Compared

Three machine learning models were evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

---

## Model Comparison Results

| Model               |   Accuracy |
| ------------------- | ---------: |
| Logistic Regression |     80.06% |
| Decision Tree       | **80.62%** |
| Random Forest       |     80.41% |

### Model Ranking

1. **Decision Tree** → **80.62%** ✅
2. Random Forest → 80.41%
3. Logistic Regression → 80.06%

---

## Best Model Selected

### Decision Tree Classifier

The Decision Tree model achieved the highest accuracy among all trained models and was selected as the final model for the churn prediction system.

### Selected Model Performance

* Accuracy: **80.62%**
* Training Set Shape: **(5634, 33)**
* Testing Set Shape: **(1409, 33)**
* Features After Encoding: **33**

---

## Model Saving

The selected Decision Tree model was saved using the `joblib` library.

### Saved File

```text
saved_models/churn_prediction_model.pkl
```

### Save Script

```text
models/save_model.py
```

The model can now be loaded later for:

* Predicting customer churn
* API integration
* Dashboard integration
* Model deployment

---

## Business Insights

### 1. Decision Tree is the best performing model

The Decision Tree model achieved the highest accuracy (**80.62%**) among all tested models.

### 2. Random Forest performed consistently

Random Forest achieved **80.41%** accuracy and provided stable predictions, but slightly underperformed compared to Decision Tree.

### 3. Logistic Regression provides a strong baseline

Logistic Regression achieved **80.06%** accuracy and serves as a simple, interpretable baseline model.

### 4. Model is deployment ready

The final model has been saved successfully and is ready for integration into APIs and dashboards.

---

## Day 11 Achievements

✅ Compared Logistic Regression, Decision Tree, and Random Forest models
✅ Selected Decision Tree as the best model
✅ Achieved **80.62%** prediction accuracy
✅ Created `model_comparison.py`
✅ Created `save_model.py`
✅ Saved the trained model as `churn_prediction_model.pkl`
✅ Prepared the project for deployment and prediction pipeline development

---

## Next Steps (Day 12)

* Load the saved model
* Build prediction pipeline
* Predict churn for new customer data
* Create `predict.py`
* Prepare model for API integration
* Begin deployment preparation

---

**Prepared By:**
**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 11
