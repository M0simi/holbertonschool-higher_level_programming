from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []

def read_csv_file():
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # --
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if int(p['id']) == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
