# Day 8 Logistic Regression Model Training Report

## Objective

Train the first Machine Learning model to predict customer churn using Logistic Regression and evaluate its performance.

---

## Dataset Information

* Total Records: **7043**
* Total Features Before Encoding: **31**
* Total Features After Encoding: **33**
* Target Variable: **Churn**

### Train-Test Split

* Training Set: **80%**
* Testing Set: **20%**

#### Training Data

* Features Shape: **(5634, 33)**
* Target Shape: **(5634, )**

#### Testing Data

* Features Shape: **(1409, 33)**
* Target Shape: **(1409, )**

---

## Model Used

### Logistic Regression

Configuration:

```python
model = LogisticRegression(
    solver="liblinear",
    max_iter=2000,
    random_state=42
)
```

---

## Model Performance

### Accuracy

```text
0.8006 (80.06%)
```

The model correctly predicted approximately **80%** of customer churn outcomes.

---

## Confusion Matrix

```text
[[937  98]
 [183 191]]
```

Interpretation:

| Actual    | Predicted Stay | Predicted Churn |
| --------- | -------------: | --------------: |
| Stay (0)  |            937 |              98 |
| Churn (1) |            183 |             191 |

---

## Classification Report

| Class     | Precision | Recall | F1-Score | Support |
| --------- | --------: | -----: | -------: | ------: |
| 0 (Stay)  |      0.84 |   0.91 |     0.87 |    1035 |
| 1 (Churn) |      0.66 |   0.51 |     0.58 |     374 |

### Overall Metrics

* Accuracy: **0.80**
* Macro Average F1-Score: **0.72**
* Weighted Average F1-Score: **0.79**

---

## Business Insights

* The Logistic Regression model achieved **80% accuracy** on the testing dataset.
* Customers who stay with the company are predicted with high accuracy.
* The model predicts churned customers reasonably well but still misses some churn cases.
* Features such as **tenure**, **contract type**, **internet service**, and **payment method** contribute significantly to churn prediction.
* This model serves as a strong baseline for comparing more advanced machine learning algorithms.

---

## Outcome

* Successfully trained the first churn prediction model.
* Evaluated model performance using accuracy, confusion matrix, and classification report.
* Established a baseline model for future comparisons.
* Prepared the project for experimenting with advanced models such as Decision Tree and Random Forest.

---

## Next Steps (Day 9)

* Train Decision Tree Classifier.
* Compare Decision Tree with Logistic Regression.
* Evaluate model performance metrics.
* Select the best performing model.

---

### Prepared By

**B. Rahul Charan Babu**
Team Lead & Member 2

**Project Day:** 8
