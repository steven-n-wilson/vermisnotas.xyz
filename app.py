
from flask import Flask, render_template
import os
import optparse

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Steven Wilson")
environment = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/speakers")
def speakers():
    return render_template("speakers.html")


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/buy-tickets")
def buy_tickets():
    return render_template("buy-tickets.html")


if __name__ == "__main__":

    debug = False

    if environment == "development" or environment == "local":
        debug = True

    app.run(host="127.0.0.1", debug=debug)
