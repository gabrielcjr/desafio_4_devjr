from domain.service.cart import cart
import infrastructure.file.file as file


class Checkout:

    _total_purchase: float = 0

    @staticmethod
    def calculate_total(cart_items):
        print(cart_items)
        if Checkout._total_purchase == 0:
            for index, item in enumerate(cart_items):
                Checkout._total_purchase += cart_items[index].subtotal

    @staticmethod
    def adjust_stock(cart_items):
        for index, items in enumerate(cart_items):
            item = cart_items[index]
            file.UpdateStock.save_product_stock(
                item.get_product.get_id, item.get_product.get_stock - int(item.get_quantity)
            )

    @staticmethod
    def place_order():
        Checkout.calculate_total(cart.items)
        Checkout.adjust_stock(cart.items)
