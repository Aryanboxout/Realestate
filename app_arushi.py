from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from flask_restful import Api, Resource
import requests

from model import Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_arushi = Blueprint('arushi', __name__,
                       url_prefix='/arushi',
                       template_folder='templates/aboutus/arushi.html',
                       static_folder='static',
                       static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_arushi)



@app_arushi.route('/arushi/', methods=['GET', 'POST'])
def arushi():
    url = "https://daysapi.p.rapidapi.com/business/delta"

    querystring = {"second_date":"2022-06-09","first_date":"2021-08-18"}

    headers = {
        'x-rapidapi-host': "daysapi.p.rapidapi.com",
        'x-rapidapi-key': "f74ed87200msh995f07c2f92be0bp101c14jsn28a6b622e01b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # return response.text
    return render_template("about us/arushi.html", stats=response.json())