import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta

# 1. Generate dummy data
num_seconds = 180  # 3 minutes of data
start_time = datetime(2026, 1, 1, 10, 0, 0)

times, rpms, speeds, mafs, throttles, loads, temps = [], [], [], [], [], [], [] #list of all the data

for i in range(num_seconds): # loop
    times.append(start_time + timedelta(seconds=i)) #
    # Normal data
    rpm = np.random.normal(2000, 100)
    speed = np.random.normal(40, 5)
    maf = np.random.normal(12, 1)
    throttle = np.random.normal(20, 2)
    load = np.random.normal(30, 3)
    temp = np.random.normal(85, 1)
    
    # Inject anomaly 1: high RPM, low speed
    if 60 <= i < 90:
        rpm = np.random.normal(7000, 50)
        speed = np.random.normal(0, 1)
    # Inject anomaly 2: wrong MAF
    if 150 <= i < 160:
        maf = np.random.normal(30, 5)

    rpms.append(rpm)
    speeds.append(speed)
    mafs.append(maf)
    throttles.append(throttle)
    loads.append(load)
    temps.append(temp)

df = pd.DataFrame({
    "time": times,
    "rpm": rpms,
    "speed": speeds,
    "maf": mafs,
    "throttle": throttles,
    "load": loads,
    "coolant_temp": temps
})

# 2. Feature engineering
df["speed_safe"] = df["speed"].replace(0, 0.1)
df["rpm_speed_ratio"] = df["rpm"] / df["speed_safe"]
df["maf_load_ratio"] = df["maf"] / (df["load"] + 0.1)

# 3. Windowing (30s)
df = df.set_index("time")  #telling the pandas that time is our main axis
windowed = df.resample("30S").agg({ #converting the 1 sec data in 30 sec chunks
    "rpm": ["mean", "max", "std"],
    "speed": ["mean", "max", "std"],
    "maf": ["mean"],
    "throttle": ["mean"],
    "load": ["mean"],
    "coolant_temp": ["mean"],
    "rpm_speed_ratio": ["mean"],
    "maf_load_ratio": ["mean"],
})
windowed.columns = ["_".join(col) for col in windowed.columns]
windowed = windowed.dropna() #Drop incomplete windows

# 4. Anomaly Detection
model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
model.fit(windowed)
windowed["anomaly"] = model.predict(windowed)

print("Detected anomaly windows:")
print(windowed[windowed["anomaly"] == -1])

# 5. Plot
plt.figure(figsize=(12,5))
plt.plot(df.index, df["rpm"], label="RPM", alpha=0.7)
plt.plot(df.index, df["speed"], label="Speed", alpha=0.7)

for t in windowed[windowed["anomaly"] == -1].index:
    plt.axvspan(t, t + pd.Timedelta(seconds=30), color="red", alpha=0.3)

plt.title("OBD-II Data with Detected Anomalies")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
