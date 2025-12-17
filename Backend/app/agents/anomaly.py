def detect_anomaly(telemetry: dict) -> dict:
    anomalies = []

    if telemetry["temp"] > 105:
        anomalies.append("ENGINE_OVERHEAT")

    if telemetry["rpm"] > 4000 and telemetry["speed"] < 30:
        anomalies.append("HIGH_RPM_LOW_SPEED")

    return {
        "is_anomaly": len(anomalies) > 0,
        "anomalies": anomalies
    }
