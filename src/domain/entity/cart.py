from dataclasses import dataclass
from typing import List
from domain.entity.item import Item
from domain.entity.product import Product


class Cart:

    __items: List[Item] = []

    def __init__(self, items: List = []) -> None:
        self.__items = items

    def add_item(self, product: Product, quantity: int):
        self.__items.append(Item(product, quantity))

    def remove_item(self, value: int):
        item_to_remove = value - 1
        Cart.__items.pop(item_to_remove)

    @property
    def items(self):
        return self.__items
