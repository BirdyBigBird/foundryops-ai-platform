from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"service": "FoundryOps AI Agent"}

@app.get("/incidents")
def incidents():
    df = pd.read_csv("../../data/raw_samples/incidents.csv")
    return df.head().to_dict()
