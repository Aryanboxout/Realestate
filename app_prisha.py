from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from flask_restful import Api, Resource
import requests

from model import Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_prisha = Blueprint('prisha', __name__,
                       url_prefix='/prisha',
                       template_folder='templates/aboutus/prisha.html',
                       static_folder='static',
                       static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_prisha)


@app_prisha.route('/prisha/', methods=['GET', 'POST'])
def prisha():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    return render_template("about us/prisha.html", stats=response.json())
    # return response.text