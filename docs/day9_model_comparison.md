# Day 9 - Model Comparison Report

## Project

**Customer Churn Prediction & Customer Lifetime Value (LTV) Engine**

---

## Objective

The objective of Day 9 was to train a **Decision Tree Classifier**, evaluate its performance, and compare it with the previously trained **Logistic Regression** model.

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

## Model 1: Logistic Regression

### Model Configuration

* Algorithm: Logistic Regression
* Solver: `liblinear`
* Random State: `42`

### Performance

* Accuracy: **80.06%**

### Confusion Matrix

```text
[[937  98]
 [183 191]]
```

### Classification Report

| Metric    | Class 0 | Class 1 |
| --------- | ------: | ------: |
| Precision |    0.84 |    0.66 |
| Recall    |    0.91 |    0.51 |
| F1-score  |    0.87 |    0.58 |

---

## Model 2: Decision Tree Classifier

### Model Configuration

* Algorithm: Decision Tree
* Criterion: `gini`
* Maximum Depth: `5`
* Random State: `42`

### Performance

* Accuracy: **80.62%**

### Confusion Matrix

```text
[[964  72]
 [201 172]]
```

### Classification Report

| Metric    | Class 0 | Class 1 |
| --------- | ------: | ------: |
| Precision |    0.83 |    0.70 |
| Recall    |    0.93 |    0.46 |
| F1-score  |    0.88 |    0.56 |

---

## Model Comparison

| Metric            | Logistic Regression | Decision Tree |
| ----------------- | ------------------: | ------------: |
| Accuracy          |              80.06% |    **80.62%** |
| Precision (Churn) |                0.66 |      **0.70** |
| Recall (Churn)    |            **0.51** |          0.46 |
| F1-Score (Churn)  |            **0.58** |          0.56 |

---

## Business Insights

### 1. Decision Tree achieved the highest accuracy

The Decision Tree model achieved **80.62% accuracy**, slightly outperforming Logistic Regression (**80.06%**).

### 2. Logistic Regression detects churn customers better

Logistic Regression achieved higher recall (**51%**) for churned customers compared to Decision Tree (**46%**), meaning it identifies more customers likely to leave.

### 3. Decision Tree predicts customer retention more accurately

Decision Tree achieved **93% recall** for customers who stay, making it highly effective at predicting retained customers.

### 4. Model selection depends on business goals

* If the goal is **maximum overall accuracy**, Decision Tree is preferred.
* If the goal is **identifying more churn-risk customers**, Logistic Regression may be preferred.

---

## Conclusion

Both machine learning models performed well on the Telco Customer Churn dataset.

* **Logistic Regression Accuracy:** 80.06%
* **Decision Tree Accuracy:** 80.62%

Decision Tree slightly outperformed Logistic Regression in overall accuracy and will be considered a strong candidate for further comparison with additional models such as **Random Forest**.

---

## Day 9 Achievements

✅ Trained Decision Tree Classifier
✅ Evaluated model using accuracy, confusion matrix, and classification report
✅ Compared Decision Tree with Logistic Regression
✅ Identified strengths and limitations of both models
✅ Generated `day9_model_comparison.md`

---

## Next Steps (Day 10)

* Train Random Forest Classifier
* Compare Random Forest with existing models
* Evaluate performance metrics
* Select the best model for deployment
* Prepare model saving pipeline

---

**Prepared By:**
**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 9
