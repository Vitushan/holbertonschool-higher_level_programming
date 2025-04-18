#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    return a welcome message
    """
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """
    return data in json
    """
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    """
    return "OK" if alright
    """
    return "OK"

@app.route('/users/<username>')
def get_users(username):
    """
    Return user info data
    """
    if not username in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username]), 200

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    add a new user in API with POST request
    """
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    return jsonify({
        'message': "User added", "user": users[username]
        }), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
