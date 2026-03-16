import pandas as pd


def explain_incident_patterns(incidents_file):

    df = pd.read_csv(incidents_file)

    most_common_severity = df["severity"].mode()[0]

    most_affected_service = df["service"].mode()[0]

    avg_resolution = df["resolution_time_minutes"].mean()

    explanation = {
        "dominant_severity": most_common_severity,
        "most_affected_service": most_affected_service,
        "average_resolution_time": avg_resolution,
        "summary": f"Most incidents are {most_common_severity} severity affecting {most_affected_service}. Average resolution time is {round(avg_resolution,2)} minutes."
    }

    return explanation


def detect_cost_anomalies(cost_file):

    df = pd.read_csv(cost_file)

    avg_cost = df["cost"].mean()

    threshold = avg_cost * 1.5

    anomalies = df[df["cost"] > threshold]

    return anomalies.to_dict(orient="records")
