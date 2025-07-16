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
        return list(reader)

@app.route('/products')
def product_display():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    products = data

    if product_id:
        selected = [p for p in products if str(p.get('id')) == str(product_id)]
        if not selected:
            return render_template('product_display.html', error="Product not found")
        products = selected

    return render_template('product_display.html', products=products)
