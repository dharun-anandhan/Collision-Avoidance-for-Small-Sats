<<<<<<< HEAD
import requests
from sgp4.io import twoline2rv
from sgp4.earth_gravity import wgs72

CELESTRAK_URL = "https://celestrak.org/NORAD/elements/stations.txt"

def fetch_tles(limit=5):
    """Fetch TLE data and parse into satellite objects."""
    response = requests.get(CELESTRAK_URL)
    lines = response.text.strip().split("\n")

    sats = []
    for i in range(0, min(limit*3, len(lines)), 3):
        name, l1, l2 = lines[i:i+3]
        sat = twoline2rv(l1, l2, wgs72)
        sats.append((name.strip(), sat))
=======
import requests
from sgp4.io import twoline2rv
from sgp4.earth_gravity import wgs72

CELESTRAK_URL = "https://celestrak.org/NORAD/elements/stations.txt"

def fetch_tles(limit=5):
    """Fetch TLE data and parse into satellite objects."""
    response = requests.get(CELESTRAK_URL)
    lines = response.text.strip().split("\n")

    sats = []
    for i in range(0, min(limit*3, len(lines)), 3):
        name, l1, l2 = lines[i:i+3]
        sat = twoline2rv(l1, l2, wgs72)
        sats.append((name.strip(), sat))
>>>>>>> 3b78c2e4b0cf568912bd8671957ca2430153fb87
    return sats