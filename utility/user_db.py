import sqlite3

con = sqlite3.connect("static/data/users.db", check_same_thread=False)
cur = con.cursor()
cur.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    name TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    cart TEXT NOT NULL
)
"""
)
con.commit()


def insert_user(name, password):
    cur.execute(
        "INSERT INTO users VALUES(:name, :password, :cart)",
        {
            "name": name,
            "password": password,
            "cart": "",
        },
    )
    con.commit()


def update_cart(new_cart: list, name):
    cur.execute(
        "UPDATE users SET cart=:cart WHERE name=:name",
        {"cart": ",".join(new_cart), "name": name},
    )
    con.commit()


def get_cart(name):
    temp = (
        cur.execute("SELECT cart FROM users WHERE name = :name", {"name": name})
        .fetchall()[0][0]
        .split(",")
    )
    return temp


def verify_password(name, password):
    try:
        temp = cur.execute(
            "SELECT password FROM users WHERE name = :name", {"name": name}
        ).fetchall()[0][0]
    except IndexError:
        return False
    return password == temp
