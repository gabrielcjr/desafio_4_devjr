from typing import List
from domain.entity.item import Item


class Cart:

    # criar um tipo para manipular quantidade e o produto
    __items: List[Item] = []

    def __init__(self, items: List = 0):
        self.__items = items

    def add_item(product: int, amount: int, products_list: dict):
        from service.products import SelectedProduct

        validated_choice: dict = SelectedProduct.selected_product(
            products_list, product, amount
        )
        Cart.__items.append(validated_choice)

    def remove_item(value):
        item_to_remove = value - 1
        Cart.__items.pop(item_to_remove)

    @property
    def items(self):
        return self.__items
