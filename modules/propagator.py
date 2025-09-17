# modules/propagator.py
from datetime import datetime, timedelta

def propagate_all(sat_objs, steps=50, interval_sec=60):
    """
    Propagate all satellites for given time steps
    """
    t0 = datetime.utcnow()
    times = [t0 + timedelta(seconds=i*interval_sec) for i in range(steps)]

    all_positions = {}
    for sat_obj in sat_objs:
        geocentric = sat_obj.at(times)
        all_positions[sat_obj.name] = geocentric

    return all_positions, times
