
from typing import List


class Cart:

    #criar um tipo para manipular quantidade e o produto
    __items: List = []

    def __init__(self, items: List):
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
    







        
        
