from flask import Flask, Response
import csv
import time

app = Flask(__name__)

def latest_row():
    try:
        with open("/data/metrics.csv") as f:
            rows = list(csv.DictReader(f))
            return rows[-1] if rows else None
    except:
        return None

@app.route("/metrics")
def metrics():
    row = latest_row()

    if not row:
        return Response("", mimetype="text/plain")

    latency = time.time() - float(row["timestamp"])

    return Response(f"""
lambda_speed_latency {latency}
temperature {row["temperature"]}
pressure {row["pressure"]}
""", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)