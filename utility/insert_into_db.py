if __name__ == "__main__":
    import sqlite3

    con = sqlite3.connect("data/items.db")
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
    curr_id = con.execute("SELECT id FROM history ORDER BY id DESC LIMIT 1").fetchall()[
        0
    ]
    for _ in range(int(input("Enter number of items to include in DB: "))):
        curr_id += 1
        name = input("Enter name of product: ")
        description = input("Enter description of product: ")
        price = int(input("Enter price of product in Rs: "))
        image = input("Enter path to image: ") or "items/default.png"
        cur.execute(
            "INSERT INTO items VALUES(:curr_id, :name, :description, :price, :image)",
            {
                "curr_id": curr_id,
                "name": name,
                "description": description,
                "price": price,
                "image": image,
            },
        )
    con.commit()
