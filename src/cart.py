
import file
import outputs_console
import outputs_web


class Cart:

    items: list = []

    @staticmethod
    def cart(product: int, amount: int, products_list: dict):
        from products import SelectedProduct
        validated_choice: dict = SelectedProduct.selected_product(
            products_list, product, amount
        )
        Cart.items.append(validated_choice)

    def add_item(self):
        pass

    def remove_item(self):
        pass

# Carregar cart instanciado , sem usar variavel de classe
cart = Cart()


class Purchase:

    _total_purchase: float = 0

    @staticmethod
    def calculate_total():
        for index, itens in enumerate(Cart.items):
            item = Cart.items[index]
            Purchase._total_purchase += item["subtotal_price"]

    @staticmethod
    def adjust_inventory():
        for index, itens in enumerate(Cart.items):
            item = Cart.items[index]
            file.UpdateInventory.save_product_inventory(item["product"], item["available_inventory"])
