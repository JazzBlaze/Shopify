from flask import Flask
from flask import render_template

# from utility import db_utilities

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
