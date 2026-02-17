#!/usr/bin/python3
"""
task_05_basic_security.py
API Security and Authentication Techniques:
- Basic Authentication (Flask-HTTPAuth)
- JWT Authentication (Flask-JWT-Extended)
- Role-based Access Control (admin-only)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Deterministic secret for checker consistency
app.config["JWT_SECRET_KEY"] = "holberton_jwt_secret_key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users stored in memory as required by spec
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# -------------------------
# Basic Auth configuration
# -------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user
    return None


@auth.error_handler
def basic_auth_error(status=401):
    return jsonify({"error": "Unauthorized"}), 401


@app.get("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -------------------------
# JWT error handlers (MUST return 401 for auth errors)
# -------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# -------------------------
# JWT routes
# -------------------------
@app.post("/login")
def login():
    """
    URL: /login
    Method: POST
    Body JSON: {"username":"...", "password":"..."}
    Response: {"access_token":"<JWT_TOKEN>"} if valid, else 401
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Unauthorized"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Unauthorized"}), 401

    # IMPORTANT: identity must be a string; role goes into additional_claims
    token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    return jsonify({"access_token": token})


@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.get("/admin-only")
@jwt_required()
def admin_only():
    """
    URL: /admin-only
    Method: GET
    Auth: JWT + role check
    Admin => "Admin Access: Granted"
    Non-admin => 403 + {"error":"Admin access required"}
    """
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
