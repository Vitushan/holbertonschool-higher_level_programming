from flask import Flask, render_template
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
    return render_template('product_display.html')
