#list of dicts - experiments
experiments = [
    {"model":"logistic_regression", "accuracy": 0.81, "loss": 0.54, "batch_size": 32, "optimizer": "adam"},
    {"model":"random_forest", "accuracy": 0.89, "loss": 0.23, "batch_size": 64, "optimizer": "sgd"},
    {"model":"gradient_boosting", "accuracy": 0.74, "loss": 0.32, "batch_size": 64, "optimizer": "adagrad"},
    {"model":"neural_net", "accuracy": 0.97, "loss": 0.10, "batch_size": 32, "optimizer": "adamax"},
    {"model":"svm", "accuracy": 0.90, "loss": 0.60, "batch_size": 128, "optimizer": "rmsprop"},
]

 #I had to google this solution and learn what lambda is, for 1 and 2. 
best_accuracy = max(experiments, key=lambda exp: exp['accuracy'])
worst_accuracy = min(experiments, key=lambda exp: exp['accuracy'])
experiments.append({"model":"knn", "accuracy": 0.70, "loss": 0.20, "batch_size": 248, "optimizer": "rmsprop"})
sum_accuracy = sum(exp["accuracy"] for exp in experiments)
len_experiments = len(experiments)
avg_accuracy = sum_accuracy / len_experiments
accuracy_sorted = sorted(experiments, key=lambda exp: exp["accuracy"])



print("==============================EXPERIMENT SUMMARY==============================")
print(f"Total runs: {len_experiments}")
print(f"Best model: {best_accuracy['model']} ({best_accuracy['accuracy']})")
print(f"Worst model: {worst_accuracy['model']} ({worst_accuracy['accuracy']})")
print(f"Avg accuracy: {avg_accuracy:.2f}")
print("====== RANKED (worst → best) ======")
for exp in accuracy_sorted:
    print(f"  {exp['model']:<25} → {exp['accuracy']:.2f}")
print("==============================================================================")

