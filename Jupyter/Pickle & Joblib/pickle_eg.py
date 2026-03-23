import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# ---------------------------
# Create Dataset
# ---------------------------

data = {
    "study_hours": [1,2,3,4,5,6,7,8,9,10],
    "attendance": [40,50,60,65,70,75,80,85,90,95],
    "assignments": [30,40,50,55,60,65,70,75,80,90],
    "result": [0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "assignments"]]
y = df["result"]

# ---------------------------
# Train Model
# ---------------------------

model = LogisticRegression()
model.fit(X, y)

# ---------------------------
# Save Model
# ---------------------------

joblib.dump(model, "student_model.pkl")

print("Model trained and saved successfully!")