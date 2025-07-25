#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},

    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity={
            "username": username,
            "role": user["role"]
        })
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_401(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_headers, jwt_payload):
    return jsonify({"error": "Token expired"}), 401


@auth.error_handler
def basic_auth_error():
    return jsonify({"error": "Unauthorized access"}), 401


if __name__ == "__main__":
    app.run()
