import os
import sys
import pytest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.entity.item import Item
from domain.entity.product import Product
from domain.entity.cart import Cart


class TestCartUnit:

    def test_constructor(self):
        print("test_constructor")
        product1 = Product(1, 'Microservices', 1.0, 99)
        item1 = Item(product1, 1)
        cart = Cart(item1)

        assert cart.items.product.get_id == 1
        assert cart.items.product.get_name == "Microservices"
        assert cart.items.product.get_price == 1.0
        assert cart.items.product.get_stock == 99
        assert cart.items.get_quantity == 1

    def test_add_item(self):
        print("test_add_item")
        cart = Cart()
        product1 = Product(1, 'Microservices', 1.0, 99)
        item1 = Item(product1, 1)
        cart.add_item(item1)
        product2 = Product(2, "Kubernetes", 2.0, 99)
        item2 = Item(product2, 1)
        cart.add_item(item2)

        assert cart.items[1].product.get_id == 2
        assert cart.items[1].product.get_name == "Kubernetes"
        assert cart.items[1].product.get_price == 2.0
        assert cart.items[1].product.get_stock == 99
        assert cart.items[1].get_quantity == 1

    def test_remove_item(self):
        print("test_remove_item")
        cart = Cart()
        product1 = Product(1, 'Microservices', 1.0, 99)
        item1 = Item(product1, 1)
        cart.add_item(item1)
        product2 = Product(2, "Kubernetes", 2.0, 99)
        item2 = Item(product2, 1)
        cart.add_item(item2)
        product3 = Product(3, "Docker", 3.0, 99)
        item3 = Item(product3, 1)
        cart.add_item(item3)
        cart.remove_item(1)

        assert cart.items[0].product.get_id == 2
        assert cart.items[0].product.get_name == "Kubernetes"
        assert cart.items[0].product.get_price == 2.0
        assert cart.items[0].product.get_stock == 99
        assert cart.items[0].get_quantity == 1
