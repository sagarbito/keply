from flask import Flask, request, jsonify

app = Flask(__name__)
users = {
    "admin@example.com": {"role": "Admin"},
    "user@example.com": {"role": "User"}
}

@app.route("/admin-data")
def admin_data():
    email = request.args.get("email")
    user = users.get(email)
    if user and user["role"] == "Admin":
        return jsonify({"data": "Sensitive admin data"})
    # ❌ Missed requirement: no logging of unauthorized attempts
    return jsonify({"error": "Unauthorized"}), 403

@app.route("/user-data")
def user_data():
    email = request.args.get("email")
    user = users.get(email)
    if user:
        return jsonify({"data": "General user data"})
    return jsonify({"error": "Unauthorized"}), 403

# ❌ Conflict: UI rendering based on roles not implemented (backend-only)
