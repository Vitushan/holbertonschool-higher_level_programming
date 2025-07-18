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
    

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'sqlite3':
        data = read_db()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        data = [product for product in data if product['id'] == product_id]
        if not data:
            return render_template('product_display.html', error='Product not found')
        return render_template('product_display.html', products=data)
    
if __name__ == '__main__':
    app.run(debug=True)
