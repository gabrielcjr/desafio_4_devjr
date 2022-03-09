from typing import Union
from outputs_web import InventoryCheck


class ProductsList:

    products: dict = {}



class SelectedProduct:

    __MINIMAL_INVENTORY_AVAILABILITY: int = 10

    @staticmethod
    def selected_product(
        products_options: dict, product_item: int, amount: int
    ) -> dict:
        for product in products_options:
            if product_item == product:
                inventory = int(products_options[product]["inventory"])
                if SelectedProduct.__inventory_check(amount, inventory):
                    price: float = products_options[product]["price"]
                    product_name: str = products_options[product]["name"]
                    return {
                        "product": product,
                        "name": product_name,
                        "price": price,
                        "subtotal_price": price * amount,
                        "amount": amount,
                        "available_inventory": inventory - int(amount),
                    }

    @classmethod
    def __inventory_check(
        self, input_amount: int, item_inventory: int
    ) -> Union[bool, None]:
        inventory: int = int(item_inventory)
        if input_amount <= (
            inventory - SelectedProduct.__MINIMAL_INVENTORY_AVAILABILITY
        ):
            return True
        InventoryCheck.inventory_not_available()
        exit(0)
