🚀 Lightweight Collision Avoidance for SmallSats

A lightweight Python-based system to simulate and visualize collision avoidance for small satellites (CubeSats, nanosats) using real Two-Line Element (TLE) data. The project propagates orbits, detects close approaches with simple methods, visualizes them in 3D, and logs results in CSV format for evaluation.

📌 Problem Statement

Low Earth Orbit (LEO) is becoming congested with satellites and debris, raising the risk of collisions. Small satellites often lack the computational power and ground control support needed for complex collision detection.
This project demonstrates a lightweight, autonomous collision avoidance approach that can run efficiently on limited hardware.

🎯 Scope

Ingest TLE datasets of satellites/debris.

Perform basic orbit propagation and close-approach estimation.

Provide simple avoidance recommendations (delta-v, hold, no action).

Store results in CSV for further analysis.

Visualize orbits in 2D/3D for demo and understanding.

💡 Solution Approach

Fetch real TLE data (from CelesTrak).

Propagate satellite orbits using skyfield.

Calculate relative distances for conjunction detection.

Store simulation results in CSV.

Plot interactive 3D visualizations of orbits for demonstration.

⚙️ Tools & Technologies

Python 3.x

Skyfield → orbit propagation

Matplotlib → 2D/3D visualization

Pandas → CSV data logging

NumPy → numerical calculations

📂 Project Structure
Collision-Avoidance-SmallSats/
│── main.py                  # Entry point for running the simulation  
│── modules/
│    ├── propagator.py        # Orbit propagation logic  
│    ├── visualization.py     # 2D/3D plotting functions  
│    ├── utils.py             # Helper functions (CSV, TLE handling)  
│── data/
│    └── satellite_positions.csv  # Output data file  
│── requirements.txt          # Python dependencies  
│── README.md                 # Project documentation  

🚀 How to Run

Clone the repository:

git clone https://github.com/your-username/Collision-Avoidance-SmallSats.git
cd Collision-Avoidance-SmallSats


Install dependencies:

pip install -r requirements.txt


Run the project:

python main.py

📊 Sample Output

3D orbital visualization of satellites.

CSV file with propagated positions.

Example log:

ISS (ZARYA) Start: [2689.05, -4263.61, 4536.37] km  
               End: [-3720.06, 4048.91, -3977.11] km  

HST          Start: [116.95, -6232.38, 3042.24] km  
               End: [-594.25, 6261.84, -2942.08] km  

📽️ Demo Video

During the demo, the system will:

Fetch TLEs of real satellites (e.g., ISS, HST).

Show propagation start and end positions.

Plot 3D orbital paths.

Explain CSV output for further analysis.

✅ Expected Outcomes

Lightweight simulation suitable for CubeSat-class hardware.

Accurate conjunction detection within simplified physics.

Easy-to-understand visualizations and CSV logs.

Scalable for future integration into autonomous satellite operations.

👥 Team Details

Team Name: Dark Cipher

Role: AI/Orbit Simulation, System Design, Visualization
