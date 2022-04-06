from itertools import product
import unittest
from unittest import mock
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.service.collection import Collection
from domain.entity.product import Product


class TestInputs(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.id = 1
        self.name = "Microservices"
        self.price = 1
        self.stock = 99
        self.products_dict = {1: {"name": "Docker", "price": 1.0, "stock": 99}}
        self.product = Product(1, "Microservices", 1, 99)

    def test_load_products_list(self):
        print("test_load_products_list")
        Collection.products_list.append(
            Product(self.id, self.name, self.price, self.stock)
        )
        actual_result = Collection.products_list[0].id
        expected_result = self.product.id
        self.assertEqual(actual_result, expected_result)
        actual_result = Collection.products_list[0].name
        expected_result = self.product.name
        self.assertEqual(actual_result, expected_result)
        actual_result = Collection.products_list[0].price
        expected_result = self.product.price
        self.assertEqual(actual_result, expected_result)
        actual_result = Collection.products_list[0].stock
        expected_result = self.product.stock
        self.assertEqual(actual_result, expected_result)

    def test_add_products(self):
        print("test_add_products")
        Collection.add_products(1, "Docker", 1.0, 99)
        actual_result = Collection.products_dict
        expected_result = self.products_dict
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
