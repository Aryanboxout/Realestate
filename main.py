# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL of server to render kangaroos.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/arushi/', methods=['GET', 'POST'])
def arushi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("arushi.html", name1=name)
    # starting and empty input default
    return render_template("arushi.html", name1="TechFish User")


@app.route('/prisha/', methods=['GET', 'POST'])
def prisha():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("prisha.html", name1=name)
    # starting and empty input default
    return render_template("prisha.html", name1="TechFish User")


@app.route('/vai/', methods=['GET', 'POST'])
def vai():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("vai.html", name1=name)
    # starting and empty input default
    return render_template("vai.html", name1="TechFish User")


@app.route('/siya/', methods=['GET', 'POST'])
def siya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("siya.html", name1=name)
    # starting and empty input default
    return render_template("siya.html", name1="TechFish User")


@app.route("/binary", methods=['GET','POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("binary.html", bits=8)


@app.route('/mini_labs/')
def mini_labs():
    return render_template("mini_labs.html")


@app.route('/explore/', methods=['GET', 'POST'])
def explore():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("explore.html", name1=name)
    # starting and empty input default
    return render_template("explore.html", name1=" ")


@app.route('/cart/', methods=['GET', 'POST'])
def cart():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("cart.html", name1=name)
    # starting and empty input default
    return render_template("cart.html", name1=" ")


@app.route('/account/', methods=['GET', 'POST'])
def account():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("account.html", name1=name)
    # starting and empty input default
    return render_template("account.html", name1=" ")

@app.route('/blog')
def blog():
    return'''
     <html>
    <head>Techfish  Home . . . Explore . . . Cart . . . Account . . . Mini Labs . . . About Us . . . </head>
    <body>
        <h2> Welcome to TechFish, the best place to buy the best waterproof tech gear! </h2>
        <p> We sell waterproof tech gear! </p>
    </body>
    </html>
    '''



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)