from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import make_response
import urllib.parse
from utility import item_db_util

app = Flask(__name__)


@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        value = request.form.get("search")
        query = urllib.parse.urlencode({"search": value}, doseq=False)
        return redirect(url_for("product") + f"?{query}")
    return render_template("home.html")


@app.route("/product", methods=["GET", "POST"])
def product():
    name = request.cookies.get("name")
    print("name", name)
    if request.method == "POST":
        value = request.form.get("search")
        query = urllib.parse.urlencode({"search": value}, doseq=False)
        return redirect(url_for("product") + f"?{query}")
    search = request.args.get("search", "")
    items = item_db_util.get_items(search)
    return render_template("product.html", items=items)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        resp = make_response(render_template("logged_in.html"))
        resp.set_cookie("name", login)
        return resp
    return render_template("login.html")
