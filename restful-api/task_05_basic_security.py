#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()




users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}



@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/login')
@auth.login_required
def login():
    return "Hello, {}!".format(auth.current_user())

@auth.get_user_roles
def get_user_roles(user):
    return user.get_roles()

@app.route('/admin')
@auth.login_required(role='admin')
def admin_only():
    return "Hello {}, you are an admin!".format(auth.current_user())

@auth.error_handler
def auth_error(status):
    return "Access Denied", status

if __name__ == "__main__":
    app.run()