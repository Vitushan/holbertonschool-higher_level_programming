from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv_file():
    products = []
    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        data = read_json_file()
    elif source == 'csv':
        data = read_csv_file()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        data = [product for product in data if product['id'] == product_id]
        if not data:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
