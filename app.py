import os
import pandas as pd
import numpy as np
import pymongo
from flask import Flask, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from bson.son import SON
app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/search-results-page.html")
def search():
    """Return the Search results page."""
    return render_template("search-results-page.html")

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

	
if __name__ == "__main__":
    app.run()
