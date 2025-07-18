from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

def read_db():
    try:
        connect = sqlite3.connect('products.de')
        cursor = connect.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        row = cursor.fetchall()
    
        product =  [{
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        }
        for row in row
    ]
        connect.close()
        return product
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None