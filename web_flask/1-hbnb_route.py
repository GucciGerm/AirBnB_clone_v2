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

if __name__ == "__main__":
        app.run()
