# Day 5 - LTV Dataset Creation

## Objective

Create a dedicated dataset for LTV modeling.

## Data Source

Telco Customer Churn Dataset

## Cleaning Steps

1. Converted TotalCharges to numeric
2. Removed missing values
3. Generated LTV feature

## LTV Formula

LTV = MonthlyCharges × tenure

## Final Dataset

File:
data/processed/ltv_dataset.csv

## Included Features

- Customer demographics
- Service information
- Revenue information
- Churn information
- Generated LTV target

## Day 5 Progress

- Generated LTV column
- Built dedicated modeling dataset
- Created ltv_dataset.csv
- Verified data quality
- Documented dataset creation