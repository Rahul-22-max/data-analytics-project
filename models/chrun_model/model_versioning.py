import os
import shutil
from datetime import datetime
import pandas as pd


def save_model_version(
    source_model_path,
    accuracy,
    algorithm="Logistic Regression",
    notes="Production model"
):
    """
    Save a versioned copy of the trained model and update the registry.
    """

    save_dir = "models/chrun_model/saved_models"
    os.makedirs(save_dir, exist_ok=True)

    registry_path = os.path.join(save_dir, "model_registry.csv")

    # -----------------------------
    # Load existing registry
    # -----------------------------
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

    # -----------------------------
    # Create versioned filename
    # -----------------------------
    date = datetime.now().strftime("%Y%m%d")

    filename = f"churn_model_v{version}_{date}.pkl"

    destination = os.path.join(save_dir, filename)

    # -----------------------------
    # Copy model
    # -----------------------------
    shutil.copy2(source_model_path, destination)

    # -----------------------------
    # Update registry
    # -----------------------------
    registry.loc[len(registry)] = [
        f"v{version}",
        filename,
        algorithm,
        round(float(accuracy), 4),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        notes
    ]

    registry.to_csv(registry_path, index=False)

    print(f"Model archived as {filename}")
    print("Registry updated successfully.")

    return destination