import pandas as pd


def analyze_incidents(file_path):

    df = pd.read_csv(file_path)

    severity_counts = df["severity"].value_counts().to_dict()

    service_failures = df["service"].value_counts().to_dict()

    avg_resolution = df["resolution_time_minutes"].mean()

    return {
        "incident_summary": severity_counts,
        "service_failure_frequency": service_failures,
        "average_resolution_time": avg_resolution
    }


def detect_deployment_failures(file_path):

    df = pd.read_csv(file_path)

    failures = df[df["status"] == "Failed"]

    return failures.to_dict(orient="records")


def telemetry_summary(file_path):

    df = pd.read_csv(file_path)

    metric_summary = df.groupby("metric")["value"].mean().to_dict()

    return metric_summary
