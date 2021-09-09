# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL of server to render kangaroos.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


# connects /walruses path to render walruses.html
@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


# connects /walruses path to render walruses.html
@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/arushi/', methods=['GET', 'POST'])
def arushi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("arushi.html", name1=name)
    # starting and empty input default
    return render_template("arushi.html", name1="World")


@app.route('/prisha/', methods=['GET', 'POST'])
def prisha():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("prisha.html", name1=name)
    # starting and empty input default
    return render_template("prisha.html", name1="World")


@app.route('/vai/', methods=['GET', 'POST'])
def vai():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("vai.html", name1=name)
    # starting and empty input default
    return render_template("vai.html", name1="World")


@app.route('/siya/', methods=['GET', 'POST'])
def siya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("siya.html", name1=name)
    # starting and empty input default
    return render_template("siya.html", name1="World")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
