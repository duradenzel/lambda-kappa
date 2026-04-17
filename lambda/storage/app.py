from flask import Flask, request

app = Flask(__name__)
storage = []

@app.route("/store", methods=["POST"])
def store():
    data = request.json
    data["timestamp_stored"] = __import__("time").time()
    storage.append(data)
    return {"status": "stored"}

@app.route("/data")
def get_data():
    return {"data": storage}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)