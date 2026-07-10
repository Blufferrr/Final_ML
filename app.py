from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load pipeline once
pipeline = joblib.load("pipeline.pkl")

# Request model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "Iris Prediction API"}

@app.post("/predict")
def predict(data: IrisInput):

    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = pipeline.predict(features)

    flowers = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
        }

    return {
        "prediction": flowers[int(prediction[0])]
            }

    
    