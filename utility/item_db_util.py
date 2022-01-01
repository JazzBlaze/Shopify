import sqlite3
from thefuzz import process
from random import sample
from utility import user_db

con = sqlite3.connect("static/data/items.db", check_same_thread=False)
cur = con.cursor()
# Initialize database if it doesn't exist
cur.execute(
    """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER(8) PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER(8),
    image TEXT DEFAULT 'items/default.png'
)
"""
)
con.commit()


def get_items(query=""):
    lst = cur.execute("SELECT * FROM items").fetchall()
    output_lst = (
        [i for i, j in process.extract(query, lst)] if query else sample(lst, len(lst))
    )
    return output_lst


def get_item_details(product_id):
    return cur.execute(
        "SELECT * FROM items WHERE id = :product_id", {"product_id": product_id}
    ).fetchall()[0]


def connect_cart_item(name):
    try:
        form_dct = dict(map(int, i.split()) for i in user_db.get_cart(name))
    except TypeError:
        form_dct = {}
    return [get_item_details(i) + tuple([form_dct[i]]) for i in form_dct]
