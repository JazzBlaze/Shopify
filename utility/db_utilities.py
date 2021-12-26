import sqlite3
from thefuzz import process
from random import sample

con = sqlite3.connect("items/items.db")
cur = con.cursor()
# Initialize database if it doesn't exist
cur.execute(
    """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER(8) PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
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
    dct_convert = [
        {"id": i1, "name": i2, "description": i3, "price": i4, "image": i5}
        for i1, i2, i3, i4, i5 in output_lst
    ]
    return dct_convert
