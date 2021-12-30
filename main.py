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
    password = request.cookies.get("password")
    if name and password:
        value = request.cookies.get("query")

        if value:
            query = urllib.parse.urlencode({"search": value}, doseq=False)
            resp = redirect(url_for("product") + f"?{query}")
            resp.set_cookie("query", "", expires=0)
            return resp

        if request.method == "POST":
            value = request.form.get("search")
            query = urllib.parse.urlencode({"search": value}, doseq=False)
            return redirect(url_for("product") + f"?{query}")

        search = request.args.get("search", "")
        items = item_db_util.get_items(search)
        return render_template("product.html", items=items)
    else:
        resp = make_response(redirect(url_for("login")))
        resp.set_cookie("query", request.args.get("search", ""))
        return resp


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        resp = make_response(render_template("logged_in.html"))
        resp.set_cookie("name", login)
        resp.set_cookie("password", password)
        return resp
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if name or password:
        return redirect(url_for("logout"))

    if request.method == "POST":
        login = request.form.get("signup")
        password = request.form.get("password")
        resp = make_response(render_template("logged_in.html"))
        resp.set_cookie("name", login)
        resp.set_cookie("password", password)
        return resp
    return render_template("signup.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if name or password:
        return render_template("logout.html")


@app.route("/logout_fr", methods=["GET", "POST"])
def logout_fr():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if name or password:
        resp = make_response(render_template("logged_out.html"))
        resp.set_cookie("name", "", expires=0)
        resp.set_cookie("password", "", expires=0)
        return resp
