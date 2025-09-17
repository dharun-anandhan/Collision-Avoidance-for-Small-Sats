from modules import config

def recommend_action(distance_km):
    """Lightweight heuristic for collision avoidance decisions."""
    if distance_km < config.CRITICAL_THRESHOLD_KM:
        return "Emergency delta-v maneuver"
    elif distance_km < config.RISK_THRESHOLD_KM * 0.6:
        return "Plan minor delta-v adjustment"
    elif distance_km < config.RISK_THRESHOLD_KM:
        return "Hold attitude, monitor closely"
    else:
        return "No action required"
