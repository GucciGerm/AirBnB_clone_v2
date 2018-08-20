#!/usr/bin/python3
from flask import Flask, render_template

"""
    This script will start a Flask web application
    Web app will be listening on 0.0.0.0 port 5000
"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def world():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def text_insert(text):
    return ("C {}".format(text).replace("_", " "))


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python_insert(text="is cool"):
    return ("Python {}".format(text).replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def num_insert(n):
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    return (render_template("5-number.html", n=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return (render_template("6-number_odd_or_even.html", n=n,
                            balance="even" if n % 2 == 0 else "odd"))


if __name__ == "__main__":
        app.run()
