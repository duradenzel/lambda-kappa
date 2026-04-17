import time
import random
import csv
import os

FILE_PATH = "/data/metrics.csv"

os.makedirs("/data", exist_ok=True)

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "pressure"])

while True:
    row = [
        time.time(),
        round(random.uniform(60, 80), 2),
        round(random.uniform(1.0, 2.0), 2)
    ]

    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print("Wrote:", row)
    time.sleep(2)