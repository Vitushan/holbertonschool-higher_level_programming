#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    def home
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    def data
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    def status
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """
    def username
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    def add user
    """
    data_user = request.get_json()
    if not data_user or 'username' not in data_user:
        return jsonify({"error": "Username is required"}), 400
    username = data_user['username']
    users[username] = data_user
    return jsonify({"message": "User added", "user": data_user}), 201


if __name__ == "__main__":
    app.run()
