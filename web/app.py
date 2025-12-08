from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        res = requests.get("http://api:5000/products")
        products = res.json()
    except:
        products = []
    html = "<h1>Products</h1><ul>"
    for p in products:
        html += f"<li>{p['name']} - ${p['price']}</li>"
    html += "</ul>"
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

