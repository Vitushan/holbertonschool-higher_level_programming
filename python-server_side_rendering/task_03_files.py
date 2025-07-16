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

    if src == 'json':
        data = read_json()
    elif src == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")
 
    product = data

    if product_id:
        select_products = []
        for product in products:
            if str(product.get('id')) == str(product_id):
                select_products.append(product)
        if not select_products:
            return render_template('product_display.html', error="Product not found")
        products = select_products
    return render_template('product_display.html', products=products)