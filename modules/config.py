# Config file to tweak thresholds (keeps system flexible but simple)

# Collision thresholds [km]
RISK_THRESHOLD_KM = 5.0       # below this → monitor carefully
CRITICAL_THRESHOLD_KM = 0.1   # below this → emergency delta-v
# Propagation time (minutes)
PROPAGATION_WINDOW = 120  # 2 hours ahead

# Step size (minutes)
STEP_SIZE = 2  # keep lightweight
# Sampling interval for propagation [seconds]
STEP_SECONDS = 60        # 1-minute steps
DURATION_MINUTES = 120   # propagate for 2 hours
OUTPUT_DIR = "outputs"
