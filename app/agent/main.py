from fastapi import FastAPI
import pandas as pd

app = FastAPI()

INCIDENT_FILE = "../../data/raw_samples/incidents.csv"
DEPLOYMENT_FILE = "../../data/raw_samples/deployments.csv"
TELEMETRY_FILE = "../../data/raw_samples/telemetry.csv"
COST_FILE = "../../data/raw_samples/costs.csv"


@app.get("/")
def root():
    return {"service": "FoundryOps AI Agent", "status": "running"}


@app.get("/incidents")
def get_incidents():
    df = pd.read_csv(INCIDENT_FILE)
    return df.to_dict(orient="records")


@app.get("/deployments")
def get_deployments():
    df = pd.read_csv(DEPLOYMENT_FILE)
    return df.to_dict(orient="records")


@app.get("/telemetry")
def get_telemetry():
    df = pd.read_csv(TELEMETRY_FILE)
    return df.to_dict(orient="records")


@app.get("/costs")
def get_costs():
    df = pd.read_csv(COST_FILE)
    return df.to_dict(orient="records")
