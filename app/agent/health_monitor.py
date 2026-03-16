import pandas as pd


def incident_volume(incidents_file):

    df = pd.read_csv(incidents_file)

    return {
        "total_incidents": len(df),
        "critical_incidents": len(df[df["severity"] == "critical"])
    }


def deployment_failure_rate(deployments_file):

    df = pd.read_csv(deployments_file)

    total = len(df)

    failures = len(df[df["status"] == "Failed"])

    rate = failures / total if total > 0 else 0

    return {
        "total_deployments": total,
        "failed_deployments": failures,
        "failure_rate": round(rate, 3)
    }


def cost_summary(cost_file):

    df = pd.read_csv(cost_file)

    return {
        "total_cost": df["cost"].sum(),
        "average_cost": df["cost"].mean(),
        "max_cost": df["cost"].max()
    }
