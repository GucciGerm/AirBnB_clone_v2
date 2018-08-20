#!/usr/bin/python3
from flask import Flask

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


if __name__ == "__main__":
        app.run()
