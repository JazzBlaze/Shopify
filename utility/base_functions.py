def calulate_price(dct: dict) -> list:
    """
    Given a dict, calculates the price
    The dictionary must contain item names as keys
    and the value must contain a dictionary having a 'quantity' and 'price' key as integers
    """
    prices: list[int] = []
    for item in dct:
        data = dct[item]
        prices.append(data["quantity"] * data["price"])
    return prices
