import string


class Item:

    product: int
    name: str
    price: float
    subtotal_price: float
    amount: float
    available_stock: int

    def __init__(
        self,
        product: int,
        name: str,
        price: float,
        subtotal_price: float,
        amount: float,
        available_stock: int,
    ):
        self.product = product
        self.name = name
        self.price = price
        self.subtotal_price = subtotal_price
        self.amount = amount
        self.available_stock = available_stock
