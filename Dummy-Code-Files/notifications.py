from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/notify")
def notify():
    return jsonify({"message": "This is a notification system"})
