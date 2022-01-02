from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import make_response
import urllib.parse
from utility import item_db_util
from utility import user_db

app = Flask(__name__)


def login_cred_template(*args, **kwargs):
    name, password = request.cookies.get("name"), request.cookies.get("password")
    logged_in = name and password and user_db.verify_password(name, password)
    kwargs["logged_in"] = bool(logged_in)
    return render_template(*args, **kwargs)


@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        value = request.form.get("search")
        if value is not None:
            query = urllib.parse.urlencode({"search": value}, doseq=False)
            return redirect(url_for("product") + f"?{query}")
        else:
            name, password = request.cookies.get("name"), request.cookies.get(
                "password"
            )
            if name and password and user_db.verify_password(name, password):
                quantity = request.form.get("quantity")
                pid = request.form.get("product_id")
                user_db.add_to_cart(int(pid), int(quantity), name)
                return redirect(url_for("product"))
            else:
                return redirect(url_for("login"))
    check_query = request.cookies.get("query")
    if check_query:
        query = urllib.parse.urlencode({"search": check_query}, doseq=False)
        resp = redirect(url_for("product") + f"?{query}")
        resp.set_cookie("query", "", expires=0)
        return resp
    return login_cred_template("home.html", items=item_db_util.get_items("")[:6])


@app.route("/product", methods=["GET", "POST"])
def product():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if name and password and user_db.verify_password(name, password):
        value = request.cookies.get("query")

        if request.method == "POST":
            value = request.form.get("search")
            if value is not None:
                query = urllib.parse.urlencode({"search": value}, doseq=False)
                return redirect(url_for("product") + f"?{query}")
            else:
                quantity = request.form.get("quantity")
                pid = request.form.get("product_id")
                user_db.add_to_cart(int(pid), int(quantity), name)
                return ("", 204)

        if value:
            query = urllib.parse.urlencode({"search": value}, doseq=False)
            resp = redirect(url_for("product") + f"?{query}")
            resp.set_cookie("query", "", expires=0)
            return resp

        search = request.args.get("search", "")
        items = item_db_util.get_items(search)
        return login_cred_template("product.html", items=items)
    else:
        resp = make_response(redirect(url_for("login")))
        resp.set_cookie("query", request.args.get("search", ""))
        return resp


@app.route("/login", methods=["GET", "POST"])
def login():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if name or password:
        if not name:
            resp = make_response(redirect(url_for("login")))
            resp.set_cookie("password", "", expires=0)
        elif not password:
            resp = make_response(redirect(url_for("login")))
            resp.set_cookie("name", "", expires=0)
        elif user_db.verify_password(name, password):
            return redirect(url_for("home"))
        else:
            resp = make_response(redirect(url_for("login")))
            resp.set_cookie("name", "", expires=0)
            resp.set_cookie("password", "", expires=0)
            return resp
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        if user_db.verify_password(login, password):
            resp = make_response(redirect(url_for("home")))
            resp.set_cookie("name", login)
            resp.set_cookie("password", password)
            return resp
        else:
            return render_template("login.html", incorrect_login=True)
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if name or password:
        if not name:
            resp = make_response(redirect(url_for("signup")))
            resp.set_cookie("password", "", expires=0)
        elif not password:
            resp = make_response(redirect(url_for("signup")))
            resp.set_cookie("name", "", expires=0)
        elif user_db.verify_password(name, password):
            return redirect(url_for("home"))
        else:
            resp = make_response(redirect(url_for("signup")))
            resp.set_cookie("name", "", expires=0)
            resp.set_cookie("password", "", expires=0)
            return resp

    if request.method == "POST":
        name = request.form.get("signup")
        password = request.form.get("password")
        if user_db.check_username_exists(name):
            return render_template("signup.html", incorrect_signup=True)
        user_db.insert_user(name, password)
        resp = make_response(redirect(url_for("home")))
        resp.set_cookie("name", name)
        resp.set_cookie("password", password)
        return resp
    return render_template("signup.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if name or password:
        return render_template("logout.html")
    else:
        return redirect(url_for("login"))


@app.route("/logout_fr", methods=["GET", "POST"])
def logout_fr():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if name or password:
        resp = make_response(redirect(url_for("home")))
        resp.set_cookie("name", "", expires=0)
        resp.set_cookie("password", "", expires=0)
        return resp
    else:
        return redirect(url_for("login"))


@app.route("/cart", methods=["GET", "POST"])
def cart():
    name = request.cookies.get("name")
    password = request.cookies.get("password")
    if not (name and password and user_db.verify_password(name, password)):
        return redirect(url_for("login"))
    if request.method == "POST":
        if request.form.get("delete_button"):
            user_db.remove_from_cart(int(request.form.get("product_id")), name)
        elif request.form.get("update_button"):
            user_db.modify_cart(
                int(request.form.get("product_id")),
                int(request.form.get("quantity")),
                name,
            )
    items = item_db_util.connect_cart_item(name)
    prices = item_db_util.calculate_prices(name)
    total = sum(prices)
    total_items = sum(int(i[4]) for i in items)
    items = tuple(i + (j,) for i, j in zip(items, prices))
    return login_cred_template(
        "cart.html", items=items, total=total, total_items=total_items
    )
