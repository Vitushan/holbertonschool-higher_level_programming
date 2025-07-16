from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def read_csv():
    with open('products.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        products = []
        for row in reader:
            try:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
            except ValueError:
                continue
            products.append(row)
        return products

@app.route('/products')
def product_display():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    products = data

    if product_id:
        try:
            product_id = int(product_id)
            selected = [p for p in products if p.get('id') == product_id]
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")
        if not selected:
            return render_template('product_display.html', error="Product not found")
        products = selected

    return render_template('product_display.html', products=products)
