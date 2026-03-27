# You ran 4 training experiments with different configs.
# Store them as a LIST OF DICTS with these fields:
# - "model_name"  (str)
# - "accuracy"    (float)
# - "loss"        (float)  
# - "batch_size"  (int)

#List of dicts
experiments = [
    {"model": "logistic_regression", "accuracy": 0.82, "loss": 0.54, "batch_size": 32 },
    {"model": "random_forest", "accuracy": 0.89, "loss": 0.39, "batch_size": 64 },
    {"model": "gradient_boosting", "accuracy": 0.91, "loss": 0.31, "batch_size": 32 },
    {"model": "neural_net", "accuracy": 0.76, "loss": 0.71, "batch_size": 128 },
]

#Challenge

#1. Print the model name of experiment 3 
print(f"Experiment 3 Model: {experiments[2]['model']}")
#Print the batch size of experiment 1
print(f"Experiment 1 Batch Size: {experiments[0]['batch_size']}")
#A 5th experiment just finised
experiments.append({"model": "svm", "accuracy": 0.86, "loss": 0.44, "batch_size": 64 })
print(f"New Experiment added: {experiments[-1]}")
#Print how many experiments you have 
print(f"Number of experiments: {len(experiments)}")
#Print all experiments except 2 
print(f"List of experiments (Except 2): {list(experiments[:1] + experiments[2:])}")
#What is the accuracy pf the last experiment in the list
print(f"Acuraccy of the last experiment in the list: {experiments[-1]['accuracy']}")



