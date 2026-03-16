from fastapi import FastAPI
import pandas as pd

from analysis_engine import (
    analyze_incidents,
    detect_deployment_failures,
    telemetry_summary
)

from ai_reasoner import (
    explain_incident_patterns,
    detect_cost_anomalies
)

from health_monitor import (
    incident_volume,
    deployment_failure_rate,
    cost_summary
)

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

@app.get("/analysis/incidents")
def incident_analysis():

    result = analyze_incidents(INCIDENT_FILE)

    return result


@app.get("/analysis/deployments")
def deployment_failures():

    result = detect_deployment_failures(DEPLOYMENT_FILE)

    return result


@app.get("/analysis/telemetry")
def telemetry_analysis():

    result = telemetry_summary(TELEMETRY_FILE)

    return result

@app.get("/analysis/explanations/incidents")
def incident_explanation():

    result = explain_incident_patterns(INCIDENT_FILE)

    return result

@app.get("/analysis/cost-anomalies")
def cost_anomalies():

    result = detect_cost_anomalies(COST_FILE)

    return result

@app.get("/health/incidents")
def health_incidents():

    result = incident_volume(INCIDENT_FILE)

    return result

@app.get("/health/deployments")
def health_deployments():

    result = deployment_failure_rate(DEPLOYMENT_FILE)

    return result

@app.get("/health/cost")
def health_cost():

    result = cost_summary(COST_FILE)

    return result
