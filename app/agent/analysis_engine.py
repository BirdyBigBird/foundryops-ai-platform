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

def detect_telemetry_anomalies(telemetry_file):

    import pandas as pd

    df = pd.read_csv(telemetry_file)

    cpu_avg = df["cpu_usage"].mean()
    mem_avg = df["memory_usage"].mean()

    cpu_threshold = cpu_avg * 1.5
    mem_threshold = mem_avg * 1.5

    anomalies = df[
        (df["cpu_usage"] > cpu_threshold) |
        (df["memory_usage"] > mem_threshold)
    ]

    return anomalies.to_dict(orient="records")
