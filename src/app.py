from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load Model
model = joblib.load("models/gridwatch_model.pkl")

# Init FastAPI App
app = FastAPI()

# Request Schema
class GridInput(BaseModel):
    GHI: float
    Temperature: float
    Relative_Humidity: float
    hour: int
    month: int

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "GridWatch API is running"}

# Prediction Endpoint
@app.post("/predict")
def predict_grid_risk(input: GridInput):
    data = pd.DataFrame([{
        "GHI": input.GHI,
        "Temperature": input.Temperature,
        "Relative Humidity": input.Relative_Humidity,
        "hour": input.hour,
        "month": input.month
    }])
    prediction = model.predict(data)[0]
    label = "High Grid Risk" if prediction == 1 else "Normal"
    return {"prediction": int(prediction), "label": label}
