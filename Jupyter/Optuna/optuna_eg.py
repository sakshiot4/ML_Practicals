import pandas as pd
import optuna
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

# Step 1: Create Data
# Here model learn Pattern So the model learns this pattern:
data = {
    'attendance': [85, 60, 72, 40, 90, 55, 82, 90, 55],
    'result': ['Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail']
}

df = pd.DataFrame(data)

X = df[['attendance']]
y = df['result']

# Step 2: Define Objective Function
def objective(trial):
    max_depth = trial.suggest_int('max_depth', 1, 56)
    criterion = trial.suggest_categorical('criterion', ['gini', 'entropy'])

    model = DecisionTreeClassifier(max_depth=max_depth, criterion=criterion)

    score = cross_val_score(model, X, y, cv=2).mean()
    return score.mean()

# Step 3: Run Optimization
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)

# Step 4: Best Parameters
print("\n\nBest parameters:", study.best_params)
print("Best score:", study.best_value)