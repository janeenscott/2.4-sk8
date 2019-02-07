from flask import Flask
from flask import request
from flask import render_template

import requests

app = Flask(__name__)


@app.route('/thank-you/', methods=['GET', 'POST'])
# configured to accept POST requests, so we can access for data (name and email) as a dictionary
def thank_you():
    print(request.form[''])
    return 'Thank you!'







#********** from planets demo
#need to switch planet api info info form
# @app.route("/")
# def index():
#     response = requests.get('https://swapi.co/api/planets/')
#
#     planets = data['results']
#
#     return render_template('index.html', planet_list=planets)