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


def insert_user(dct):
    cur.execute(
        "INSERT INTO users VALUES(:name, :password, :cart)",
        {
            "name": dct["name"],
            "password": dct["password"],
            "cart": "",
        },
    )


def update_cart(new_cart: list, name):
    cur.execute(
        "UPDATE users SET cart=:cart WHERE name=:name",
        {"cart": ",".join(new_cart), "name": name},
    )


def get_cart(name):
    temp = (
        cur.execute("SELECT cart FROM users WHERE name = :name", {"name": name})
        .fetchall()[0][0]
        .split(",")
    )
    return temp
