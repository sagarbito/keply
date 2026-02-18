from flask import Flask, jsonify

app = Flask(__name__)
tasks = [{"id":1,"title":"Sample","done":True},{"id":2,"title":"Another","done":False}]
login_frequency = {"test@example.com": 5}  # ❌ Requirement: should be tracked dynamically

@app.route("/dashboard")
def dashboard():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    completion_rate = (completed / total) * 100 if total else 0
    return jsonify({
        "total_tasks": total,
        "completed_tasks": completed,
        "completion_rate": f"{completion_rate:.2f}%",
        "recent_activity": tasks[-5:],
        "login_frequency": login_frequency  # ❌ Partial: static, no charts, no CSV export
    })
