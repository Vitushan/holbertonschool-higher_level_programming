#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""


from flask import Flask
from flask import jsonify, json, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    """
    return a welcome message
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    """
    return data in json
    """
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """
    return "OK" if alright"
    """
    return "OK"

@app.route("/users/<username>")

def users(username):
    """
    Return user info data
    """
    if username in users:
        return jsonify(users[username])
    else:
        return ({"error": "User not found"}), 404

@app.route("/add_user")
def add_user():
    """
    ...
    """
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400




if __name__ == "__main__":
    app.run(debug=True)
