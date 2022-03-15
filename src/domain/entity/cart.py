import sys
import os

currentdir = f'{os.path.dirname(os.path.realpath(__file__))}/../../'
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import infrastructure.file.file as file


class Cart:

    items: list = []
    

    @staticmethod
    def cart(product: int, amount: int, products_list: dict):
        from service.products import SelectedProduct
        validated_choice: dict = SelectedProduct.selected_product(
            products_list, product, amount
        )
        Cart.items.append(validated_choice)

    def add_item(self):
        pass

    def remove_item(self):
        pass

# Carregar cart instanciado , sem usar variavel de classe
# cart = Cart()


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
            item = Cart.items[index]
            file.UpdateStock.save_product_stock(item["product"], item["available_stock"])
    
    @staticmethod
    def place_order():
        Checkout.calculate_total(Cart.items)
        Checkout.adjust_stock(Cart.items)
        
        
