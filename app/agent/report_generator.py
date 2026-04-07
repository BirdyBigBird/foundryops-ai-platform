import pandas as pd

def generate_operational_report(
    incidents_file,
    deployments_file,
    telemetry_file,
    cost_file
):

    incidents = pd.read_csv(incidents_file)
    deployments = pd.read_csv(deployments_file)
    telemetry = pd.read_csv(telemetry_file)
    costs = pd.read_csv(cost_file)

    report = {}

    # Incident summary
    report["incident_summary"] = {
        "total": len(incidents),
        "by_severity": incidents["severity"].value_counts().to_dict()
    }

    # Deployment health
    total_deployments = len(deployments)
    failed = len(deployments[deployments["status"] == "Failed"])

    report["deployment_health"] = {
        "total": total_deployments,
        "failed": failed,
        "failure_rate": round(failed / total_deployments, 3) if total_deployments > 0 else 0
    }

    # Telemetry overview
    report["telemetry"] = {
        "avg_cpu": round(telemetry["cpu_usage"].mean(), 2),
        "avg_memory": round(telemetry["memory_usage"].mean(), 2)
    }

    # Cost overview
    report["cost"] = {
        "total_cost": round(costs["cost"].sum(), 2),
        "avg_cost": round(costs["cost"].mean(), 2)
    }

    # Executive summary (THIS is key)
    report["summary"] = (
        f"{report['incident_summary']['total']} incidents recorded. "
        f"{failed} failed deployments detected. "
        f"Average CPU usage is {report['telemetry']['avg_cpu']}%. "
        f"Total cost is {report['cost']['total_cost']}."
    )

    return report
