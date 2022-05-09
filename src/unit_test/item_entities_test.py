import os
import sys
import pytest
from src.domain.entity.product import Product
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.entity.item import Item


class TestCartUnit:

    def test_constructor(self):
        print("test_constructor")
        item = Item(Product(1, 'Microservices', 2.0, 99), 2)

        assert item.product.get_id == 1
        assert item.product.get_name == "Microservices"
        assert item.product.get_price == 2.0
        assert item.product.get_stock == 99
        assert item.get_quantity == 2
        assert item.get_product == Product(id=1, name='Microservices', price=2.0, stock=99)
        assert item.subtotal == 4.0
