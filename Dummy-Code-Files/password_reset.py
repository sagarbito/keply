from flask import Flask, request, jsonify
import uuid, time

app = Flask(__name__)
reset_tokens = {}
users = {"test@example.com": {"password_hash": "hashedpassword123"}}

@app.route("/reset-request", methods=["POST"])
def reset_request():
    email = request.form.get("email")
    if email in users:
        token = str(uuid.uuid4())
        reset_tokens[token] = {"email": email, "expiry": time.time() + 900}
        print(f"Reset link sent to {email} with token {token}")
    return jsonify({"message": "Reset link sent"}), 200

@app.route("/reset-password", methods=["POST"])
def reset_password():
    token = request.form.get("token")
    new_password = request.form.get("password")
    if token not in reset_tokens:
        return jsonify({"error": "Invalid token"}), 400
    if time.time() > reset_tokens[token]["expiry"]:
        del reset_tokens[token]
        return jsonify({"error": "Token expired"}), 400
    email = reset_tokens[token]["email"]
    # ❌ Missed requirement: should hash password before storing
    users[email]["password_hash"] = new_password
    # ❌ Missed requirement: no logging of reset attempts
    del reset_tokens[token]
    return jsonify({"message": "Password updated"}), 200
