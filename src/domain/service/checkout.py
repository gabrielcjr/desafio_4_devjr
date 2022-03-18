import infrastructure.file.file as file
from domain.service.cart import cart


class Checkout:


    _total_purchase: float = 0

    @staticmethod
    def calculate_total(value):
        if Checkout._total_purchase == 0:
            for item in value:
                Checkout._total_purchase += item["subtotal_price"]

    
    @staticmethod
    def adjust_stock(value):
        for index, items in enumerate(value):
            cart_items = cart.items
            item = cart_items[index]
            file.UpdateStock.save_product_stock(
                item["product"], item["available_stock"]
            )

    @staticmethod
    def place_order():
        Checkout.calculate_total(cart.items)
        Checkout.adjust_stock(cart.items)
