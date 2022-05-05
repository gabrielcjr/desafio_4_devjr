from dataclasses import is_dataclass
import os
import sys
import unittest

from src.domain.entity.product import Product
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


class TestCartUnit(unittest.TestCase):
    def test_if_it_is_a_dataclass(self):
        print("test_if_it_is_a_dataclass")
        self.assertTrue(is_dataclass(Product))

    def test_constructor(self):
        print("test_constructor")
        product = Product(1, 'Microservices', 2.0, 99)

        self.assertEqual(product.get_id, 1)
        self.assertEqual(product.get_name, "Microservices")
        self.assertEqual(product.get_price, 2.0)
        self.assertEqual(product.get_stock, 99)

    def test_increment_stock(self):
        print("test_increment_stock")
        product = Product(1, 'Microservices', 2.0, 99)
        product.increment_stock(1)

        self.assertEqual(product.get_stock, 100)

    def test_decrement_stock(self):
        print("test_decrement_stock")
        product = Product(1, 'Microservices', 2.0, 99)
        product.decrement_stock(1)

        self.assertEqual(product.get_stock, 98)

        with self.assertRaises(Exception) as assert_error:
            product.decrement_stock(100)
        self.assertEqual(assert_error.exception.args[0], "Stock must be greater or equal than 0")
