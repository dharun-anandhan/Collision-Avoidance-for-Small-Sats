<<<<<<< HEAD
from skyfield.api import EarthSatellite, load

def load_tles(filename):
    """Load TLEs from file and return list of (name, EarthSatellite object)."""
    sats = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):  # every 3 lines = name + 2 TLE lines
            name = lines[i].strip()
            l1 = lines[i+1].strip()
            l2 = lines[i+2].strip()
            sat = EarthSatellite(l1, l2, name, load.timescale())
            sats.append((name, sat))
    return sats
=======
from skyfield.api import EarthSatellite, load

def load_tles(filename):
    """Load TLEs from file and return list of (name, EarthSatellite object)."""
    sats = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):  # every 3 lines = name + 2 TLE lines
            name = lines[i].strip()
            l1 = lines[i+1].strip()
            l2 = lines[i+2].strip()
            sat = EarthSatellite(l1, l2, name, load.timescale())
            sats.append((name, sat))
    return sats
>>>>>>> 3b78c2e4b0cf568912bd8671957ca2430153fb87
