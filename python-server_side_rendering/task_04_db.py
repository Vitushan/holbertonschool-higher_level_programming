from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)

def read_db():
    try:
        connect = sqlite3.connect('products.de')
        cursor = connect.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
    except sqlite3.Error as e: