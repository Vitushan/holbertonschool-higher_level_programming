#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""


from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def home(self):
    return "Welcome to the Flask API !."


if __name__ == "__main__":
    app.run(debug=True)
