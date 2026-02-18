from flask import Flask, request, session, redirect, jsonify
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "supersecret"

# Simulated DB
users = {"test@example.com": {"password_hash": "hashedpassword123"}}

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400
    
    user = users.get(email)
    if user and check_password_hash(user["password_hash"], password):
        session["user"] = email
        return redirect("/dashboard")
    return jsonify({"error": "Invalid credentials"}), 401
