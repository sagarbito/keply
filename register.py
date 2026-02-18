from flask import Flask, request, redirect, jsonify
from werkzeug.security import generate_password_hash

app = Flask(__name__)
users = {}

@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400
    
    if email in users:
        return jsonify({"error": "Email already exists"}), 400
    
    if len(password) < 8:
        return jsonify({"error": "Weak password"}), 400
    
    users[email] = {"password_hash": generate_password_hash(password)}
    # Simulate sending confirmation email
    print(f"Confirmation email sent to {email}")
    return redirect("/login")
