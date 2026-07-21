import subprocess
import sys

def run_script(script_name):
    """Run a Python script and stop if it fails."""
    print(f"\nRunning {script_name}...")

    result = subprocess.run(
        [sys.executable, f"models/chrun_model/{script_name}"],
        check=False
    )

    if result.returncode != 0:
        print(f"{script_name} failed.")
        sys.exit(result.returncode)

    print(f"{script_name} completed successfully.")


def main():
    print("=" * 50)
    print("Customer Churn Model Retraining Pipeline")
    print("=" * 50)

    # Step 1: Train model
    run_script("train.py")

    # Step 2: Evaluate trained model
    run_script("model_monitor.py")

    print("\nPipeline completed successfully!")
    print("Latest model has been trained, versioned, and evaluated.")


if __name__ == "__main__":
    main()