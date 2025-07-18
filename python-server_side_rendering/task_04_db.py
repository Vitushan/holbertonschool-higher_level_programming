from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

def read_db():
    try:
        connect = sqlite3.connect('products.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
    
        products =  [{
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        }
        for row in rows]

        connect.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None