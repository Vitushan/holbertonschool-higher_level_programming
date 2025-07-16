from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


@app.route('/product_display')
def product_display():
    src = request.args.get('src')
    product_id = request.args.get('id')

    if src == 'json':
        products = read_json()
    elif src == 'csv':
        products = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")
 
    if product_id:
        select_products = []
        for product in products:
            if str(product.get('id')) == str(product_id):
                select_products.append(product)
        if not select_products:
            return render_template('product_display.html', error="Product not found")
        products = select_products
    return render_template('product_display.html', products=products)