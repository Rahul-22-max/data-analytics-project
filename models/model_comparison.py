import pandas as pd

# Model names and accuracies

models = {
    "Logistic Regression": 0.8006,
    "Decision Tree": 0.8062,
    "Random Forest": 0.8041
}

print("===== MODEL COMPARISON =====\n")

# Display all model accuracies

for model, accuracy in models.items():

    print(
        f"{model:<22}: {accuracy:.4f}"
    )

# Find best model

best_model = max(
    models,
    key=models.get
)

best_accuracy = models[best_model]

print("\n===== BEST MODEL =====\n")

print("Model:")

print(best_model)

print("\nAccuracy:")

print(
    round(best_accuracy, 4)
)

print("\n===== MODEL RANKING =====\n")

ranking = sorted(
    models.items(),
    key=lambda x: x[1],
    reverse=True
)

for i, (model, accuracy) in enumerate(
    ranking,
    start=1
):

    print(
        f"{i}. {model} -> {accuracy:.4f}"
    )

print("\nDay 11 Model Comparison Completed!")