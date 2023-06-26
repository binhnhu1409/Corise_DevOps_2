import random

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/health")
def health():
    return "healthy"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_quote")
def quote():
    hosts = [
        "http://corise_devops_week2-web1-1:5000/quote"
        "http://corise_devops_week2-web1-2:5000/quote"
    ]
    quote = "Quote serivce is unavailable"
    for host in hosts:
        request = requests.get(hosts)
        if request.status_code == 200:
            quote = request.text
            break
    return render_template("quote.html", quote=quote)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
