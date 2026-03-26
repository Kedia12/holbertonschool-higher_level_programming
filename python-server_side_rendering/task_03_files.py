from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    data = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return data


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 🔴 Mauvais source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 🔹 Lire data
    try:
        if source == 'json':
            data = read_json()
        else:
            data = read_csv()
    except Exception:
        return render_template('product_display.html', error="Error reading data")

    # 🔹 Filtrer par id
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]

            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid id")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)