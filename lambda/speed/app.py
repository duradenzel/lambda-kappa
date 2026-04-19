from flask import Flask, Response
import csv
import time

app = Flask(__name__)

def latest_row():
    try:
        with open("/data/metrics.csv") as f:
            rows = [r for r in csv.DictReader(f) if r.get("timestamp", "").strip()]
            return rows[-1] if rows else None
    except Exception as e:
        print("Error reading CSV:", e)
        return None

@app.route("/metrics")
def metrics():
    row = latest_row()
    if not row:
        return Response("", mimetype="text/plain")

    try:
        latency = time.time() - float(row["timestamp"].strip())
        temperature = float(row["temperature"].strip())
        pressure = float(row["pressure"].strip())
    except (KeyError, ValueError) as e:
        print("Error parsing row:", e, row)
        return Response("", mimetype="text/plain")

    return Response(f"""\
lambda_speed_latency {latency}
temperature {temperature}
pressure {pressure}
""", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)