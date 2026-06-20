# Day 10 - Random Forest Model Report

## Project

**Customer Churn Prediction & Customer Lifetime Value (LTV) Engine**

---

## Objective

The objective of Day 10 was to train a **Random Forest Classifier**, evaluate its performance, and compare it with the previously trained **Logistic Regression** and **Decision Tree** models.

---

## Dataset Information

* Dataset Name: `cleaned_telco_customer_churn.csv`
* Total Records: **7043**
* Total Features Before Encoding: **31**
* Total Features After Encoding: **33**
* Training Set Size: **5634**
* Testing Set Size: **1409**
* Train-Test Split Ratio: **80:20**

---

## Model: Random Forest Classifier

### Model Configuration

* Algorithm: Random Forest Classifier
* Number of Trees (`n_estimators`): **100**
* Maximum Depth (`max_depth`): **10**
* Random State: **42**

---

## Model Performance

### Accuracy

**80.41%**

---

### Confusion Matrix

```text id="qj7nq7"
[[949  87]
 [189 184]]
```

---

### Classification Report

| Metric    | Class 0 | Class 1 |
| --------- | ------: | ------: |
| Precision |    0.83 |    0.68 |
| Recall    |    0.92 |    0.49 |
| F1-score  |    0.87 |    0.57 |

**Overall Accuracy:** **80.41%**

---

## Comparison with Previous Models

| Model               |   Accuracy |
| ------------------- | ---------: |
| Logistic Regression |     80.06% |
| Decision Tree       | **80.62%** |
| Random Forest       |     80.41% |

### Ranking

1. **Decision Tree** → **80.62%** ✅
2. **Random Forest** → **80.41%**
3. **Logistic Regression** → **80.06%**

---

## Business Insights

### 1. Random Forest performed consistently

Random Forest achieved **80.41% accuracy**, making it the second-best model among the three tested models.

### 2. Decision Tree remains the best model

Decision Tree achieved the highest accuracy (**80.62%**) and currently remains the best performing model.

### 3. Logistic Regression detects churn slightly better

Logistic Regression achieved slightly higher recall for churn customers, making it useful when the business goal is to identify more customers likely to leave.

### 4. Ensemble methods provide stable performance

Random Forest combines multiple decision trees and provides stable predictions while reducing overfitting.

---

## Conclusion

The Random Forest model successfully predicted customer churn with **80.41% accuracy**.

Although its performance was slightly lower than the Decision Tree model, it remains a strong candidate due to its robustness and ability to reduce overfitting.

Current best model:

**Decision Tree Classifier (80.62% Accuracy)** ✅

---

## Day 10 Achievements

✅ Trained Random Forest Classifier
✅ Achieved **80.41%** model accuracy
✅ Generated confusion matrix and classification report
✅ Compared Random Forest with Logistic Regression and Decision Tree
✅ Identified the current best model
✅ Generated `day10_random_forest.md`

---

## Next Steps (Day 11)

* Compare all machine learning models in detail
* Select the final best model
* Save the trained model using `joblib`
* Prepare model for API deployment
* Begin prediction pipeline development

---

**Prepared By:**
**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 10
