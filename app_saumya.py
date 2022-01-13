from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from flask_restful import Api, Resource
import requests

from model import Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_saumya = Blueprint('saumya', __name__,
                      url_prefix='/saumya',
                      template_folder='templates/aboutus/saumya.html',
                      static_folder='static',
                      static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_saumya)

@app_saumya.route('/saumya/', methods=['GET', 'POST'])
def saumya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("about us/saumya.html", name1=name)
    # starting and empty input default
    return render_template("about us/saumya.html", name1="TechFish User")