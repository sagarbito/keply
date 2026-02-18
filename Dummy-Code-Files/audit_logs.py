from flask import Flask, jsonify

app = Flask(__name__)
logs = []

@app.route("/log", methods=["POST"])
def log_event():
    event = {"action": "login_attempt", "status": "failed"}
    logs.append(event)
    return jsonify({"message": "Event logged"}), 201

@app.route("/logs")
def get_logs():
    return jsonify(logs)
