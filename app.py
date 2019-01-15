from flask import Flask
from flask import request
from flask import render_template

import requests

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get('https://swapi.co/api/planets/')

    planets = data['results']

    return render_template('index.html', planet_list=planets)