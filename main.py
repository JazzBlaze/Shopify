from flask import Flask
from flask import render_template
from utility import db_utilities

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("hello.html")
