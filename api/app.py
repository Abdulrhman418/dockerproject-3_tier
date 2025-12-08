from flask import Flask, jsonify
import mysql.connector
from decimal import Decimal

app = Flask(__name__)

@app.route("/products")
def get_products():

    conn = mysql.connector.connect(
        host="db-tair",
        user="root",
        password="root123",
        database="products_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products")
    rows = cursor.fetchall()

    rows_serializable = [{"id": r[0], "name": r[1], "price": float(r[2])} for r in rows]

    cursor.close()
    conn.close()

    return jsonify(rows_serializable)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

