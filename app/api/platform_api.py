from fastapi import FastAPI
import requests

app = FastAPI()

AGENT_URL = "http://localhost:8000"


@app.get("/")
def root():

    return {
        "service": "FoundryOps Platform API",
        "status": "running"
    }


@app.get("/platform/incidents")
def incidents():

    response = requests.get(f"{AGENT_URL}/analysis/incidents")

    return response.json()


@app.get("/platform/deployments")
def deployments():

    response = requests.get(f"{AGENT_URL}/analysis/deployments")

    return response.json()


@app.get("/platform/telemetry")
def telemetry():

    response = requests.get(f"{AGENT_URL}/analysis/telemetry")

    return response.json()

@app.get("/platform/health/incidents")
def platform_health_incidents():

    response = requests.get(f"{AGENT_URL}/health/incidents")

    return response.json()

@app.get("/platform/health/deployments")
def platform_health_deployments():

    response = requests.get(f"{AGENT_URL}/health/deployments")

    return response.json()

@app.get("/platform/health/cost")
def platform_health_cost():

    response = requests.get(f"{AGENT_URL}/health/cost")

    return response.json()
