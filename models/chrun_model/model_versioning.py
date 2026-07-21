import os
import sys
import shutil
from datetime import datetime
import pandas as pd

# ==========================================================
# Add Project Root to Python Path
# ==========================================================
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# Import Configuration
# ==========================================================
from config.config import VERSION_DIR


def save_model_version(
    source_model_path,
    accuracy,
    algorithm="Logistic Regression",
    notes="Production model"
):
    """
    Save a versioned copy of the trained model and update
    the model registry.
    """

    # Create version directory if it doesn't exist
    os.makedirs(VERSION_DIR, exist_ok=True)

    registry_path = os.path.join(
        VERSION_DIR,
        "model_registry.csv"
    )

    # ------------------------------------------------------
    # Load existing registry
    # ------------------------------------------------------
    if os.path.exists(registry_path):
        registry = pd.read_csv(registry_path)
        version = len(registry) + 1
    else:
        registry = pd.DataFrame(columns=[
            "Version",
            "Model File",
            "Algorithm",
            "Accuracy",
            "Training Date",
            "Notes"
        ])
        version = 1

    # ------------------------------------------------------
    # Create versioned filename
    # ------------------------------------------------------
    current_date = datetime.now().strftime("%Y%m%d")

    model_filename = (
        f"churn_model_v{version}_{current_date}.pkl"
    )

    destination = os.path.join(
        VERSION_DIR,
        model_filename
    )

    # ------------------------------------------------------
    # Copy latest model
    # ------------------------------------------------------
    shutil.copy2(
        source_model_path,
        destination
    )

    # ------------------------------------------------------
    # Create new registry record
    # ------------------------------------------------------
    new_record = {
        "Version": f"v{version}",
        "Model File": model_filename,
        "Algorithm": algorithm,
        "Accuracy": round(float(accuracy), 4),
        "Training Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Notes": notes
    }

    registry = pd.concat(
        [registry, pd.DataFrame([new_record])],
        ignore_index=True
    )

    # ------------------------------------------------------
    # Save registry
    # ------------------------------------------------------
    registry.to_csv(
        registry_path,
        index=False
    )

    print(f"Model archived as {model_filename}")
    print("Registry updated successfully.")

    return destination


# ==========================================================
# Run only when executed directly
# ==========================================================
if __name__ == "__main__":
    print("Model Versioning Module")