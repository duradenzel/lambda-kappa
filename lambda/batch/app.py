from flask import Flask, Response
import csv
import time
import threading

app = Flask(__name__)

latest = {
    "timestamp": time.time(),
    "temperature": 0.0,
    "pressure": 0.0,
    "batch_time": time.time()
}

def worker():
    global latest
    while True:
        try:
            with open("/data/metrics.csv") as f:
                rows = [r for r in csv.DictReader(f) if r.get("timestamp", "").strip()]
                if rows:
                    row = rows[-1]
                    latest = {
                        "timestamp": float(row["timestamp"].strip()),
                        "temperature": float(row["temperature"].strip()),
                        "pressure": float(row["pressure"].strip()),
                        "batch_time": time.time()
                    }
        except Exception as e:
            print("Error in worker:", e)
        time.sleep(10)

@app.route("/metrics")
def metrics():
    try:
        latency = latest["batch_time"] - latest["timestamp"]
    except (KeyError, ValueError) as e:
        print("Error computing latency:", e)
        return Response("", mimetype="text/plain")

    return Response(f"""\
lambda_batch_latency {latency}
temperature_batch {latest["temperature"]}
pressure_batch {latest["pressure"]}
""", mimetype="text/plain")

if __name__ == "__main__":
    threading.Thread(target=worker, daemon=True).start()
    app.run(host="0.0.0.0", port=5002)