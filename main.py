from modules.satellite import Satellite
from modules import propagator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import numpy as np

# Distance threshold for conjunction alert (km)
CONJUNCTION_THRESHOLD = 10.0

# Example TLE data (can replace with real Starlink, ISS, etc.)
TLE_DATA = [
    ('ISS (ZARYA)',
     '1 25544U 98067A   25001.12345678  .00001234  00000-0  12345-3 0  9991',
     '2 25544  51.6446  12.3456 0006789 123.4567 321.6543 15.49567890123456'),
    ('HST',
     '1 20580U 90037B   25001.12345678  .00000123  00000-0  12345-3 0  9992',
     '2 20580  28.4697  42.1234 0003210 321.4567 123.6543 15.00012345678901')
]

def fetch_satellites():
    return [Satellite(name, l1, l2) for name, l1, l2 in TLE_DATA]

def detect_conjunctions(propagated, threshold=CONJUNCTION_THRESHOLD):
    conjunctions = {}
    names = list(propagated.keys())
    num_steps = propagated[names[0]].shape[0]
    for t_idx in range(num_steps):
        for i in range(len(names)):
            for j in range(i+1, len(names)):
                sat1 = names[i]
                sat2 = names[j]
                pos1 = propagated[sat1][t_idx]
                pos2 = propagated[sat2][t_idx]
                dist = np.linalg.norm(pos1 - pos2)
                if dist <= threshold:
                    action = "Delta-v maneuver suggested"
                    conjunctions[(t_idx, sat1)] = action
                    conjunctions[(t_idx, sat2)] = action
    return conjunctions

def save_to_csv(propagated, times, conjunctions, filename='satellite_positions.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Time', 'Satellite', 'X_km', 'Y_km', 'Z_km', 'Conjunction', 'Action'])
        for t_idx, t in enumerate(times):
            for sat_name, positions in propagated.items():
                x, y, z = positions[t_idx]
                key = (t_idx, sat_name)
                if key in conjunctions:
                    writer.writerow([t.isoformat(), sat_name, x, y, z, "YES", conjunctions[key]])
                else:
                    writer.writerow([t.isoformat(), sat_name, x, y, z, "NO", "No action"])
    print(f"\nData saved to {filename}")

def plot_3d(propagated, conjunctions=None):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    for sat_name, positions in propagated.items():
        x = positions[:, 0]
        y = positions[:, 1]
        z = positions[:, 2]
        ax.plot(x, y, z, label=sat_name)
        ax.scatter(x[0], y[0], z[0], marker='o')  # start
        ax.scatter(x[-1], y[-1], z[-1], marker='x')  # end
    if conjunctions:
        for (t_idx, sat_name), action in conjunctions.items():
            pos = propagated[sat_name][t_idx]
            ax.scatter(pos[0], pos[1], pos[2], color='r', s=50, alpha=0.7)
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title('3D Orbits with Conjunctions')
    ax.legend()
    plt.show()

def main():
    print("🚀 Lightweight Collision Avoidance for SmallSats\n")
    sats = fetch_satellites()
    print(f"Fetched {len(sats)} satellites")

    propagated, times = propagator.propagate_all(sats)

    for name, pos in propagated.items():
        print(f"{name} Start: {pos[0]} km | End: {pos[-1]} km")

    conjunctions = detect_conjunctions(propagated)
    save_to_csv(propagated, times, conjunctions)
    plot_3d(propagated, conjunctions)

if __name__ == "__main__":
    main()
