from flask import Flask, render_template
import json
import csv

app = Flask(__name__)


@app.route('/product_display')
def product_display(force=False, silent=False):
    with open('product_display', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return render_template('product_display.html', product_display=data.get('product_display'))

    with open('product_display', 'r', encoding='utf-8'):
        data = csv.dumps(f)
        return render_template('product_display.html', product_display=data.get('product_display'))


