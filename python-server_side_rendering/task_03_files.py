from flask import Flask, render_template
import json
import csv

app = Flask(__name__)


@app.route('/product_display')
def read_json():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def read_csv():
    with open('data.csv', 'r', encoding='utf-8'):
        reader = csv.DictReader(f)
        return reader

