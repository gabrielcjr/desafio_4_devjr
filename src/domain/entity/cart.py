from typing import List
from domain.entity.item import Item


class Cart:

    _items: List[Item] = []

    def __init__(self, items: List = []) -> None:
        self._items = items

    def add_item(self, new_item: Item):
        self._items.append(new_item)

    def remove_item(self, value: int):
        item_to_remove = value - 1
        self._items.pop(item_to_remove)

    @property
    def items(self):
        return self._items
