#ML: Context you just ran 5 experiments and recorded accurary scores

print("===========================List Exercise===========================")


experiment_scores = [0.72, 0.85, 0.91, 0.78, 0.88] 

experiment_scores.append(0.95) #Append a new experiment to the list

#1. What is the score of the first experiment
print(f"First Experiment: {experiment_scores[0]}")

#2. What was the score of the last experiment 
print(f"Last Experiment: {experiment_scores[-1]}")

#3. What were the scores of experiments 2 through 4 (middle 3)
print(f"Experiments 2-4: {experiment_scores[1:4]}")

#4. How many experiments did you run 
print(f"Total Experiments: {len(experiment_scores)}")

#5. What is the highest score
print(f"Highest Score: {max(experiment_scores)}")

#6 What was the lowest score 
print(f"Lowest Score: {min(experiment_scores)}")

#Print the experiments worst to best 
print(f"Worst - Best Rank: {sorted(experiment_scores)}")

#Print avg score
avg = sum(experiment_scores) / len(experiment_scores)
print(f"The avarage score is: {avg:.2f}")

print("===========================Dict Exercise===========================")

model_a = {"accuracy": 0.91, "loss": 0.43, "optimizer": "adam"}
model_b= {"accuracy": 0.85, "loss": 0.61, "optimizer": "sgd"}
model_c = {"accuracy": 0.78, "loss": 0.74, "optimizer": "adam"}

print("==========================Models==========================")
print(model_a)
print(model_b)
print(model_c)
print("=========================================================")

#1 Print models B accuracy 
print(f"Model B Accuracy: {model_b['accuracy']}")

#2 Add 50 epochs to model A
model_a["epochs"] = 50
print(f"Model A Epochs: {model_a['epochs']}")

#Print all keys in model C
print(f"Keys of model C: {list(model_c.keys())}")

#Check if loss is in model b 
print(f"Loss in model B: {'loss' in model_b}")




