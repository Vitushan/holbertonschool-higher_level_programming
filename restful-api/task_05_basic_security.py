#!/usr/bin/python3
"""
security API with Flask
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
"""
docstring
"""
app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    """
    verify password for basic auth
    """
    if username in users and \
        check_password_hash(
            users[username]["password"], password):
        return username
    return None


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def basic_protected():
    """
    login Basic protected
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    endpoint for post login data
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    role = user['role']
    access_token = create_access_token(
        identity=username, additional_claims={"role": role})
    return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    JWT protected route
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    only admin route
    """
    claims = get_jwt()
    role = claims.get("role")
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Forbidden authorized
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    invalid handle token error
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    expired handle token error
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Handle revoked token error
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    """
    Handle fresh token required error
    """
    return jsonify({"error": "Fresh token required"}), 401


@jwt.unauthorized_loader
def handle_missing_token(err):
    """error handling"""
    return jsonify({"error": "Authorization header missing or invalid"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    """error handling"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.invalid_token_loader
def handle_invalid_claims(err):
    """error handling"""
    return jsonify({"error": "Invalid token claims"}), 401


if __name__ == "__main__":
    app.run()
