print('System Monitor Ready')
import psutil
import datetime

# Log file path
log_file = "logs/system_stats.log"

# Collect system stats
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Timestamp
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write stats to log file
with open(log_file, "a") as f:
    f.write(f"{time_now} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%\n")

print("System stats logged successfully!")
