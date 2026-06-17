# Day 7 Machine Learning Preparation Report

## Objective

Prepare the processed customer churn dataset for Machine Learning model development.

---

## Dataset Information

* Total Records: **7043**
* Total Features Before Split: **31**
* Total Features After Encoding: **33**
* Target Variable: **Churn**

---

## Train-Test Split

The dataset was divided into:

* Training Set: **80%**
* Testing Set: **20%**

### Training Data

* Features Shape: **(5634, 33)**
* Target Shape: **(5634, )**

### Testing Data

* Features Shape: **(1409, 33)**
* Target Shape: **(1409, )**

---

## Data Preparation Steps

1. Loaded processed dataset.
2. Separated features (`X`) and target (`y`).
3. Applied one-hot encoding to categorical features.
4. Performed train-test split using:

* `test_size = 0.2`
* `random_state = 42`
* `stratify = y`

---

## Outcome

The dataset is now fully prepared for Machine Learning model development.

Member 3 can directly use the training and testing datasets for churn prediction model development.

---

**Prepared By:**
B. Rahul Charan Babu
Team Lead & Member 2

**Project Day:** 7
