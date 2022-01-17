from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from flask_restful import Api, Resource
import requests

from model import Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_vidhi = Blueprint('vidhi', __name__,
                     url_prefix='/vidhi',
                     template_folder='templates/aboutus/vidhi.html',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_vidhi)

@app_vidhi.route('/vidhi/', methods=['GET', 'POST'])
def vidhi():

    url = "https://world-clock.p.rapidapi.com/json/utc/now"

    headers = {
        'x-rapidapi-host': "world-clock.p.rapidapi.com",
        'x-rapidapi-key': "b7497e5bbbmsh13875b44b129b4dp1a492fjsnf27f047e11f5"
    }

    response = requests.request("GET", url, headers=headers)
    return render_template("about us/vidhi.html", stats=response.json())