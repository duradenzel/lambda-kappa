import time
import random
import csv
import os
import math

FILE_PATH = "/data/metrics.csv"

os.makedirs("/data", exist_ok=True)

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "event_time", "temperature", "pressure"])

step = 0

while True:
    t = time.time()

  
    base_temp = 70 + 8 * math.sin(2 * math.pi * step / 30)
    base_pressure = 1.5 + 0.3 * math.sin(2 * math.pi * step / 30 + math.pi)

    if step % 60 == 0 and step > 0:
        base_temp += random.uniform(15, 25)
        base_pressure += random.uniform(0.4, 0.7)
        print(f"[ANOMALY INJECTED] step={step}")

    temperature = round(base_temp + random.gauss(0, 0.5), 4)
    pressure = round(base_pressure + random.gauss(0, 0.02), 4)

    row = [t, t, temperature, pressure]

    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print(f"Wrote: step={step} ts={t:.2f} temp={temperature} pressure={pressure}")

    step += 1
    time.sleep(2)