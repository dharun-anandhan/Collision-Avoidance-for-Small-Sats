# demo.py
import sys
from datetime import datetime
from tle_parser import read_tle_file, fetch_tles
from propagator import sample_times, propagate_positions
from conjunction import find_min_separation, risk_score
from avoidance import recommend_action


# Fetch fresh TLEs from Celestrak (default: ISS + stations)
tle_path = fetch_tles()
objs = read_tle_file(tle_path)


now = datetime.utcnow()


# sample 1h forward, 10s step for speed in demo
times = sample_times(now, window_seconds=3600, step_seconds=10)


for i in range(len(objs)):
for j in range(i+1, len(objs)):
sat1 = objs[i]['satrec']
sat2 = objs[j]['satrec']
r1, v1 = propagate_positions(sat1, times)
r2, v2 = propagate_positions(sat2, times)
info = find_min_separation(times, r1, v1, r2, v2)
tca = info['tca']
miss_km = info['miss_km']
relspeed = info['rel_speed_km_s']
tca_seconds = (tca - now).total_seconds()
score = risk_score(miss_km, relspeed, tca_seconds)
action = recommend_action(miss_km, relspeed, tca, now)
print('PAIR:', objs[i]['name'], objs[j]['name'])
print(' TCA:', tca, 'miss_km=%.3f' % miss_km, 'rel_speed_km_s=%.5f' % relspeed)
print(' RISK_SCORE:', score)
print(' RECOMMENDATION:', action)
print()