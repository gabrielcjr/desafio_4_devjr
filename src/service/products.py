from typing import Union
from template.outputs_web import StockCheck
from entity.product import Product


class ProductsList:

    
    products: dict = {}
    



class SelectedProduct:

    __MINIMAL_STOCK_AVAILABILITY: int = 10

    @staticmethod
    def selected_product(
        products_options: dict, product_item: int, amount: int
    ) -> dict:
        for product in products_options:
            if product_item == product:
                stock = int(products_options[product]["stock"])
                if SelectedProduct.__stock_check(amount, stock):
                    price: float = products_options[product]["price"]
                    product_name: str = products_options[product]["name"]
                    return {
                        "product": product,
                        "name": product_name,
                        "price": price,
                        "subtotal_price": price * amount,
                        "amount": amount,
                        "available_stock": stock - int(amount),
                    }

    @classmethod
    def __stock_check(
        self, input_amount: int, item_stock: int
    ) -> Union[bool, None]:
        stock: int = int(item_stock)
        if input_amount <= (
            stock - SelectedProduct.__MINIMAL_STOCK_AVAILABILITY
        ):
            return True
        StockCheck.stock_not_available()
        exit(0)
