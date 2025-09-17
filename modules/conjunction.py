<<<<<<< HEAD
# modules/conjunction.py
import numpy as np
from modules import config

def find_min_separation(times, pos1, pos2):
    """Find minimum distance, time of closest approach, and relative speed."""
    dists = np.linalg.norm(pos1 - pos2, axis=1)
    idx = int(np.nanargmin(dists))
    miss_km = float(dists[idx])
    tca = times[idx]

    # Estimate relative speed (finite difference)
    dt = (times[1] - times[0]).total_seconds() if len(times) > 1 else 60.0
    if 0 < idx < len(times)-1:
        relv = ((pos2[idx+1] - pos1[idx+1]) - (pos2[idx-1] - pos1[idx-1])) / (2*dt)
    else:
        relv = (pos2[min(idx+1,len(times)-1)] - pos1[min(idx+1,len(times)-1)]) - \
               (pos2[max(idx-1,0)] - pos1[max(idx-1,0)])
        relv = relv / dt
    rel_speed = float(np.linalg.norm(relv))

    return {'miss_km': miss_km, 'tca': tca, 'rel_speed_km_s': rel_speed}


def likely_colocated(name1, name2, rel_speed):
    """Filter pairs that are known to be docked or modules of the same station."""
    n1, n2 = name1.upper(), name2.upper()
    station_keywords = ["ISS", "NAUKA", "PROGRESS", "SOYUZ", 
                        "TIANHE", "WENTIAN", "MENGTIAN", "TIANZHOU", "SHENZHOU"]
    for k in station_keywords:
        if k in n1 and k in n2:
            return True
    if rel_speed < 0.001:  # <1 m/s relative → probably docked
        return True
    return False


def decide_action(miss_km):
    """Decide avoidance action based on thresholds."""
    if miss_km < config.CRITICAL_THRESHOLD_KM:
        return "Emergency delta-v maneuver"
    elif miss_km < config.RISK_THRESHOLD_KM:
        return "Delta-v adjustment"
    else:
        return "No action"


def detect_conjunctions(propagated, times):
    """Main detection loop for all pairs."""
    sats = list(propagated.keys())
    results = []
    for i in range(len(sats)):
        for j in range(i+1, len(sats)):
            s1, s2 = sats[i], sats[j]
            pos1, pos2 = propagated[s1], propagated[s2]

            if pos1.shape[0] == 0 or pos2.shape[0] == 0:
                continue

            info = find_min_separation(times, pos1, pos2)
            miss, tca, rel_speed = info['miss_km'], info['tca'], info['rel_speed_km_s']

            if likely_colocated(s1, s2, rel_speed):
                continue  # skip docked pairs

            if miss < config.RISK_THRESHOLD_KM:
                action = decide_action(miss)
                results.append({
                    'sat1': s1, 'sat2': s2,
                    'miss_km': round(miss, 3),
                    'tca': tca,
                    'rel_speed_km_s': round(rel_speed, 4),
                    'action': action
                })
    return results
=======
# modules/conjunction.py
import numpy as np
from modules import config

def find_min_separation(times, pos1, pos2):
    """Find minimum distance, time of closest approach, and relative speed."""
    dists = np.linalg.norm(pos1 - pos2, axis=1)
    idx = int(np.nanargmin(dists))
    miss_km = float(dists[idx])
    tca = times[idx]

    # Estimate relative speed (finite difference)
    dt = (times[1] - times[0]).total_seconds() if len(times) > 1 else 60.0
    if 0 < idx < len(times)-1:
        relv = ((pos2[idx+1] - pos1[idx+1]) - (pos2[idx-1] - pos1[idx-1])) / (2*dt)
    else:
        relv = (pos2[min(idx+1,len(times)-1)] - pos1[min(idx+1,len(times)-1)]) - \
               (pos2[max(idx-1,0)] - pos1[max(idx-1,0)])
        relv = relv / dt
    rel_speed = float(np.linalg.norm(relv))

    return {'miss_km': miss_km, 'tca': tca, 'rel_speed_km_s': rel_speed}


def likely_colocated(name1, name2, rel_speed):
    """Filter pairs that are known to be docked or modules of the same station."""
    n1, n2 = name1.upper(), name2.upper()
    station_keywords = ["ISS", "NAUKA", "PROGRESS", "SOYUZ", 
                        "TIANHE", "WENTIAN", "MENGTIAN", "TIANZHOU", "SHENZHOU"]
    for k in station_keywords:
        if k in n1 and k in n2:
            return True
    if rel_speed < 0.001:  # <1 m/s relative → probably docked
        return True
    return False


def decide_action(miss_km):
    """Decide avoidance action based on thresholds."""
    if miss_km < config.CRITICAL_THRESHOLD_KM:
        return "Emergency delta-v maneuver"
    elif miss_km < config.RISK_THRESHOLD_KM:
        return "Delta-v adjustment"
    else:
        return "No action"


def detect_conjunctions(propagated, times):
    """Main detection loop for all pairs."""
    sats = list(propagated.keys())
    results = []
    for i in range(len(sats)):
        for j in range(i+1, len(sats)):
            s1, s2 = sats[i], sats[j]
            pos1, pos2 = propagated[s1], propagated[s2]

            if pos1.shape[0] == 0 or pos2.shape[0] == 0:
                continue

            info = find_min_separation(times, pos1, pos2)
            miss, tca, rel_speed = info['miss_km'], info['tca'], info['rel_speed_km_s']

            if likely_colocated(s1, s2, rel_speed):
                continue  # skip docked pairs

            if miss < config.RISK_THRESHOLD_KM:
                action = decide_action(miss)
                results.append({
                    'sat1': s1, 'sat2': s2,
                    'miss_km': round(miss, 3),
                    'tca': tca,
                    'rel_speed_km_s': round(rel_speed, 4),
                    'action': action
                })
    return results
>>>>>>> 3b78c2e4b0cf568912bd8671957ca2430153fb87
