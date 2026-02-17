#!/usr/bin/python3
"""
task_04_flask.py
Simple REST API using Flask.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# NOTE: Keep this empty when pushing to avoid checker issues
users = {}


@app.get("/")
def home():
    return "Welcome to the Flask API!"


@app.get("/status")
def status():
    return "OK"


@app.get("/data")
def data():
    """Return a list of all usernames stored in memory."""
    return jsonify(list(users.keys()))


@app.get("/users/<username>")
def get_user(username):
    """Return the full user object for the given username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.post("/add_user")
def add_user():
    """
    Add a new user.
    Expected JSON:
      {"username": "...", "name": "...", "age": ..., "city": "..."}
    """
    # Validate JSON body
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Build stored user object (include username in the object)
    user_obj = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    # Running directly: python3 task_04_flask.py
    app.run()
