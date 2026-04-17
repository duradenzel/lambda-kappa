from flask import Flask, Response
import csv
import time
import threading

app = Flask(__name__)

latest = {}

def worker():
    global latest
    while True:
        try:
            with open("/data/metrics.csv") as f:
                rows = list(csv.DictReader(f))
                if rows:
                    latest = rows[-1]
                    latest["batch_time"] = time.time()
        except Exception as e:
            print(e)

        time.sleep(10)

@app.route("/metrics")
def metrics():
    if not latest:
        return Response("", mimetype="text/plain")

    latency = float(latest["batch_time"]) - float(latest["timestamp"])

    return Response(f"""
lambda_batch_latency {latency}
temperature_batch {latest["temperature"]}
pressure_batch {latest["pressure"]}
""", mimetype="text/plain")

if __name__ == "__main__":
    threading.Thread(target=worker, daemon=True).start()
    app.run(host="0.0.0.0", port=5002)