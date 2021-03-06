import os
import pandas as pd
from flask import Flask, render_template

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
    # Cambiar segun la clase que se quiere desplegar
    df = pd.read_pickle('MC 006, section B, Fall 2019')
    return render_template("ver-notas.html", df=df.to_html(classes='table', header='true'))


if __name__ == "__main__":

    debug = False

    if environment == "development" or environment == "local":
        debug = True

    app.run(host="127.0.0.1", debug=debug)
