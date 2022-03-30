import string
from dataclasses import dataclass


@dataclass()
class Item:

    product: int
    name: str
    price: float
    subtotal_price: float
    amount: float
    available_stock: int
