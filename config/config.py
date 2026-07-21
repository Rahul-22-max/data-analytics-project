import os

# ==========================================================
# Base Project Directory
# ==========================================================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ==========================================================
# Dataset
# ==========================================================
DATA_PATH = os.path.join(
    BASE_DIR,
    "Data",
    "processed",
    "cleaned_telco_customer_churn.csv"
)

# ==========================================================
# Model Directories
# ==========================================================
MODEL_DIR = os.path.join(BASE_DIR, "models", "chrun_model")
MODEL_PATH = os.path.join(MODEL_DIR, "churn_model.pkl")
VERSION_DIR = os.path.join(MODEL_DIR, "saved_models")

# ==========================================================
# Reports
# ==========================================================
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

FEATURE_IMPORTANCE_PATH = os.path.join(
    REPORTS_DIR,
    "logistic_feature_importance.csv"
)

MODEL_REPORT_PATH = os.path.join(
    REPORTS_DIR,
    "model_performance_report.md"
)

METRICS_PATH = os.path.join(
    REPORTS_DIR,
    "model_metrics.csv"
)

# ==========================================================
# Logs
# ==========================================================
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "api.log")

# ==========================================================
# Train/Test Split
# ==========================================================
TEST_SIZE = 0.20
RANDOM_STATE = 42

# ==========================================================
# Logistic Regression Parameters
# ==========================================================
MAX_ITER = 2000
SOLVER = "liblinear"

# ==========================================================
# Create Required Directories
# ==========================================================
for directory in [
    MODEL_DIR,
    VERSION_DIR,
    REPORTS_DIR,
    LOG_DIR
]:
    os.makedirs(directory, exist_ok=True)