import psutil
import os
import time

def log_performance(tag="Run"):
    """Log lightweight performance stats for CPU & memory."""
    process = psutil.Process(os.getpid())
    cpu_percent = psutil.cpu_percent(interval=0.2)
    mem_info = process.memory_info().rss / (1024 * 1024)  # MB
    return {
        "tag": tag,
        "cpu_percent": cpu_percent,
        "memory_mb": round(mem_info, 2),
        "timestamp": time.strftime("%H:%M:%S")
    }
