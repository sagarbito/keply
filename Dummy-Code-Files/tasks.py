from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["POST"])
def create_task():
    title = request.form.get("title")
    description = request.form.get("description", "")
    due_date = request.form.get("due_date", "")
    
    if not title:
        return jsonify({"error": "Title required"}), 400
    
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "done": False
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = request.form.get("title", task["title"])
            task["description"] = request.form.get("description", task["description"])
            task["done"] = request.form.get("done", str(task["done"])) == "True"
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200
