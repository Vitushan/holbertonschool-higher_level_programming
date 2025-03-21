from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    """Read product data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data():
    """Read product data from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id to int and price to float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []

def read_sql_data():
    """Read product data from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # This enables column access by name
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        
        # Convert SQLite Row objects to dictionaries
        products = []
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
            
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

@app.route('/products')
def products():
    # Get query parameters
    source = request.args.get('source', '')
    product_id = request.args.get('id')
    
    # Initialize variables
    products_data = []
    error_message = None
    
    # Read data based on source parameter
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    elif source == 'sql':
        products_data = read_sql_data()
    else:
        error_message = "Wrong source"
    
    # Filter by id if provided
    if product_id and not error_message:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p['id'] == product_id]
            
            if filtered_products:
                products_data = filtered_products
            else:
                error_message = "Product not found"
                products_data = []
        except ValueError:
            error_message = "Invalid ID format"
            products_data = []
    
    # Render template with data and any error messages
    return render_template('product_display.html', 
                          products=products_data, 
                          error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)