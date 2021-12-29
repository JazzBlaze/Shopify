from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from utility import db_utilities

app = Flask(__name__)


@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        value = request.form.get("search")
        return redirect(url_for("product") + f"?search={value}")
    return render_template("home.html")


@app.route("/product", methods=["GET", "POST"])
def product():
    search = request.args.get("search", "")
    items = db_utilities.get_items(search)
    return render_template("product.html", items=items)
