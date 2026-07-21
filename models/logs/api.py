from logger import logger
logger.info("Prediction request received")

prediction = model.predict(customer_df)[0]
probability = float(model.predict_proba(customer_df)[0][1])

logger.info(
    f"Prediction={prediction}, Probability={probability:.4f}"
)

try:
    prediction = model.predict(customer_df)[0]
    probability = float(model.predict_proba(customer_df)[0][1])

    logger.info(
        f"Prediction={prediction}, Probability={probability:.4f}"
    )

    return {
        "prediction": int(prediction),
        "churn_probability": probability
    }

except Exception as e:
    logger.error(str(e))
    return {
        "error": str(e)
    }