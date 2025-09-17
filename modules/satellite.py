# modules/satellite.py
from sgp4.api import Satrec, jday
import numpy as np
from datetime import datetime, timedelta

class Satellite:
    def __init__(self, name, tle_line1, tle_line2):
        self.name = name
        self.satrec = Satrec.twoline2rv(tle_line1, tle_line2)

    def propagate(self, dt_seconds, epoch=None):
        """
        Returns geocentric (x, y, z) in km for dt_seconds after epoch
        """
        if epoch is None:
            epoch = datetime.utcnow()
        t = epoch + timedelta(seconds=dt_seconds)
        jd, fr = jday(t.year, t.month, t.day, t.hour, t.minute, t.second + t.microsecond*1e-6)
        e, r, v = self.satrec.sgp4(jd, fr)
        if e != 0:
            return np.array([np.nan, np.nan, np.nan])
        return np.array(r)  # km

    def at(self, times):
        positions = []
        for t in times:
            dt = (t - times[0]).total_seconds()
            pos = self.propagate(dt, times[0])
            positions.append(pos)
        return np.array(positions)
