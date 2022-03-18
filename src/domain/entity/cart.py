from typing import List
from domain.entity.item import Item


class Cart:

    # criar um tipo para manipular quantidade e o produto
    __items: List[Item] = []

    def __init__(self, items: List = 0):
        self.__items = items

    def add_item(self, item: dict):
        self.__items.append(item)

    def remove_item(self, value: int):
        item_to_remove = value - 1
        Cart.__items.pop(item_to_remove)

    @property
    def items(self):
        return self.__items
