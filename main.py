from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
# import "packages" from flask
from flask import Flask, render_template, request
import requests
import http.client

from flask import render_template
from __init__ import app

# from starter.starter import app_starter
# from algorithm.algorithm import app_algorithm
from app_crud import app_crud
# from y2022 import app_y2022

# # create a Flask instance
# app = Flask(__name__)

# app.register_blueprint(app_starter)
# app.register_blueprint(app_algorithm)
app.register_blueprint(app_crud)
# app.register_blueprint(app_y2022)

# connects default URL of server to render kangaroos.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    return render_template("attendance.html")


@app.route('/to_do_list', methods=['GET', 'POST'])
def to_do_list():
    return render_template("to_do_list.html")


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": "san diego", "lat": "0", "lon": "0", "lang": "en", "units": "imperial"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "f74ed87200msh995f07c2f92be0bp101c14jsn28a6b622e01b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return render_template("/weather.html", stats=response.json())
    #return response.text


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("quiz.html", name1=name)
    # starting and empty input default
    return render_template("quiz.html", name1="TechFish User")


@app.route('/googlemap')
def googlemap():
    return render_template("locations.html")


@app.route('/phonestablets')
def phonestablets():
    return render_template("departments/phonestablets.html")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html")

@app.route('/desktopstvs')
def desktopstvs():
    return render_template("departments/desktopstvs.html")


@app.route('/audiodevices')
def audiodevices():
    return render_template("departments/audiodevices.html")


@app.route('/aidevices')
def aidevices():
    return render_template("departments/aidevices.html")


@app.route("/binary", methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("mini labs/binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("mini labs/binary.html", bits=8)


@app.route("/colors", methods=['GET', 'POST'])
def colors():
    return render_template("mini labs/colorcodes.html")


@app.route('/addition')
def addition():
    return render_template("mini labs/addition.html")


@app.route("/logicgates", methods=['GET', 'POST'])
def logicgates():
    return render_template("mini labs/logicgates.html")


@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("API/joke.html", joke=response.json())


@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("API/jokes.html", jokes=response.json())


@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """
    return render_template("API/covid19.html", stats=response.json())
    # return response.text

@app.route('/rgb/')
def rgb():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('mini labs/rgb.html', images=image_data(path))


@app.route('/arushirgb/')
def arushirgb():
    path = Path(app.root_path) / "static" / "arushiassets"
    return render_template('about us/templates/rgb/arushirgb.html', images=arushi_image_data(path))


@app.route('/prishargb/')
def prishargb():
    path = Path(app.root_path) / "static" / "prishaassets"
    return render_template('about us/templates/rgb/prishrgb.html', images=prisha_image_data(path))


@app.route('/vaishavirgb/')
def vaishavirgb():
    path = Path(app.root_path) / "static" / "vaishaviassets"
    return render_template('about us/templates/rgb/vaishavirgb.html', images=vaishavi_image_data(path))


@app.route('/siyargb/')
def siyargb():
    path = Path(app.root_path) / "static" / "siyaassets"
    return render_template('about us/templates/rgb/siyargb.html', images=siya_image_data(path))


@app.route('/AboutUs/', methods=['GET', 'POST'])
def AboutUs():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("about us/MainAboutUs.html", name1=name)
    # starting and empty input default
    return render_template("about us/MainAboutUs.html", name1="TechFish User")


@app.route('/arushi/', methods=['GET', 'POST'])
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



# @app.route('/prisha/', methods=['GET', 'POST'])
# def prisha():
#     # submit button has been pushed
#     if request.form:
#         name = request.form.get("name")
#         if len(name) != 0:  # input field has content
#             return render_template("about us/prisha.html", name1=name)
#     # starting and empty input default
#     return render_template("about us/prisha.html", name1="TechFish User")


@app.route('/prisha/', methods=['GET', 'POST'])
def prisha():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    return render_template("about us/prisha.html", stats=response.json())
    # return response.text


@app.route('/vidhi/', methods=['GET', 'POST'])
def vidhi():

    url = "https://world-clock.p.rapidapi.com/json/utc/now"

    headers = {
        'x-rapidapi-host': "world-clock.p.rapidapi.com",
        'x-rapidapi-key': "b7497e5bbbmsh13875b44b129b4dp1a492fjsnf27f047e11f5"
    }

    response = requests.request("GET", url, headers=headers)
    return render_template("about us/vidhi.html", stats=response.json())


@app.route('/saumya/', methods=['GET', 'POST'])
def saumya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("about us/saumya.html", name1=name)
    # starting and empty input default
    return render_template("about us/saumya.html", name1="TechFish User")


@app.route('/aryan/', methods=['GET', 'POST'])
def aryan():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("about us/aryan.html", name1=name)
    # starting and empty input default
    return render_template("about us/aryan.html", name1="TechFish User")

@app.route('/saumyaapi', methods=['GET', 'POST'])
def saumyaapi():

    #greet function
    #set variables = number; input
    # set lat/lon = variable name

    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

    querystring = {"lat":"35.5","lon":"-78.5"}

    headers = {
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
        'x-rapidapi-key': "8d571b2f72msh44f8fd48e083624p19cce1jsnfb1e373c1716"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # return(response.text)
    return render_template("api/saumyaapi.html", stats=response.json())

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")



@app.route('/aryansapi', methods=['GET', 'POST'])
def aryansapi():

    url = "https://allah-name.p.rapidapi.com/name"

    headers = {
        'x-rapidapi-host': "allah-name.p.rapidapi.com",
        'x-rapidapi-key': "a53d1a4acemsh90db192dc27d5f7p1028a2jsn2e483944f85c"
    }

    response = requests.request("GET", url, headers=headers)
    return render_template("api/aryansapi.html", stats=response.json())


@app.route('/studytimer', methods=['GET', 'POST'])
def studytimer():
    return render_template("studytimer.html")


@app.route('/pagetwo', methods=['GET', 'POST'])
def pagetwo():
    return render_template("pagetwo.html")


@app.route('/crud', methods=['GET', 'POST'])
def crud():
    return render_template("crud.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template("search.html")

@app.route('/DNHSinformative', methods=['GET', 'POST'])
def DNHSinformative():
    return render_template("DNHSinformative.html")


#
# @app.route('/calender', methods=['GET', 'POST'])
# def calender():
#     return render_template("calender.html")

if __name__ == "__main__":
    app.run(debug=True, port=5222)