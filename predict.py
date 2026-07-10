import joblib
from sklearn.datasets import load_iris

# Load pipeline
pipeline = joblib.load("pipeline.pkl")

# Sample input
sample = [[5.1, 3.5, 1.4, 0.2]]

# Predict
prediction = pipeline.predict(sample)

# Convert prediction number to flower name
iris = load_iris()

print("Prediction:", iris.target_names[prediction[0]])