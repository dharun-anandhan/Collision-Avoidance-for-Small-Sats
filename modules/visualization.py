<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

def plot_orbits(propagated, risky_pairs):
    """2D plot of orbits and highlight risky conjunctions."""
    plt.figure(figsize=(8, 8))
    
    for sat, positions in propagated.items():
        if len(positions) > 0:
            xs = [p[0] for p in positions]
            ys = [p[1] for p in positions]
            plt.plot(xs, ys, label=sat, alpha=0.7)

    # Highlight risky pairs
    for sat1, sat2, dist in risky_pairs:
        p1 = propagated[sat1][0]
        p2 = propagated[sat2][0]
        plt.scatter(p1[0], p1[1], color="red", s=50, marker="x")
        plt.scatter(p2[0], p2[1], color="red", s=50, marker="x")
        plt.text(p1[0], p1[1], f"⚠ {sat1} vs {sat2}\n{dist:.2f} km", fontsize=8)

    plt.xlabel("X (km)")
    plt.ylabel("Y (km)")
    plt.title("Satellite Orbits & Risky Conjunctions")
    plt.legend()
    plt.grid(True)
    plt.show()
=======
import matplotlib.pyplot as plt
import numpy as np

def plot_orbits(propagated, risky_pairs):
    """2D plot of orbits and highlight risky conjunctions."""
    plt.figure(figsize=(8, 8))
    
    for sat, positions in propagated.items():
        if len(positions) > 0:
            xs = [p[0] for p in positions]
            ys = [p[1] for p in positions]
            plt.plot(xs, ys, label=sat, alpha=0.7)

    # Highlight risky pairs
    for sat1, sat2, dist in risky_pairs:
        p1 = propagated[sat1][0]
        p2 = propagated[sat2][0]
        plt.scatter(p1[0], p1[1], color="red", s=50, marker="x")
        plt.scatter(p2[0], p2[1], color="red", s=50, marker="x")
        plt.text(p1[0], p1[1], f"⚠ {sat1} vs {sat2}\n{dist:.2f} km", fontsize=8)

    plt.xlabel("X (km)")
    plt.ylabel("Y (km)")
    plt.title("Satellite Orbits & Risky Conjunctions")
    plt.legend()
    plt.grid(True)
    plt.show()
>>>>>>> 3b78c2e4b0cf568912bd8671957ca2430153fb87
