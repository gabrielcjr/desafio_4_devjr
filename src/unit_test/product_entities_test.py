from dataclasses import is_dataclass
import os
import sys
import pytest

from src.domain.entity.product import Product
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


class TestCartUnit:
    def test_if_it_is_a_dataclass(self):
        print("test_if_it_is_a_dataclass")
        assert is_dataclass(Product) == True

    def test_constructor(self):
        print("test_constructor")
        product = Product(1, 'Microservices', 2.0, 99)

        assert product.get_id == 1
        assert product.get_name == "Microservices"
        assert product.get_price == 2.0
        assert product.get_stock == 99

    def test_increment_stock(self):
        print("test_increment_stock")
        product = Product(1, 'Microservices', 2.0, 99)
        product.increment_stock(1)

        assert product.get_stock == 100

    def test_decrement_stock(self):
        print("test_decrement_stock")
        product = Product(1, 'Microservices', 2.0, 99)
        product.decrement_stock(1)

        assert product.get_stock == 98

        with pytest.raises(Exception) as assert_error:
            product.decrement_stock(100)
        assert str(assert_error.value) == "Stock must be greater or equal than 0"
