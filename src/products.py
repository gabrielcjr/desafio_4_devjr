from typing import Union
from outputs_web import InventoryCheck


class ProductsList:

    products: dict = {}

    @staticmethod
    def products_list(dict: dict):
        list_products: str = ""
        for product in dict:
            name: str = dict[product]["name"]
            price: float = dict[product]["price"]
            list_products += "<a href=\"cart\%s\">%s - %s $ %.2f</a><br>" % (product, product, name, price)
        return list_products


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
