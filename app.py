
from flask import Flask, render_template
import os
import optparse

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Steven Wilson")
environment = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nosotros")
def about():
    return render_template("nosotros.html")


@app.route("/ver-notas")
def buy_tickets():
    return render_template("ver-notas.html")


if __name__ == "__main__":

    debug = False

    if environment == "development" or environment == "local":
        debug = True

    app.run(host="127.0.0.1", debug=debug)
