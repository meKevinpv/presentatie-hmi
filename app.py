from datetime import datetime
from distutils.log import error
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/HMI/<id>")
def hmi(id = None):
    return render_template("machine.html",
    id = id,
    date = datetime.now(),
    error = False)


@app.route("/HMI/<id>/error")
def hmi_error(id = None):
    return render_template("machine.html",
    id = id,
    date = datetime.now(),
    error = True)

