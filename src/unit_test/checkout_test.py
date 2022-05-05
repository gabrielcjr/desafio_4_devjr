import unittest
from unittest import mock
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.service.checkout import Checkout
from domain.entity.item import Item
from domain.entity.product import Product

BASE_PATH = os.path.abspath(os.path.dirname(__file__))


def open_file(mode):
    return open(f"{BASE_PATH}/_stock_file2.txt", mode)


def read_lines():
    file = open_file("r")
    lines = file.readlines()
    file.close()
    return lines


class TestInputs(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.cart_items: list = [
            Item(product=Product(id=1, name='Microservices', price=1.0, stock=95), quantity=1),
            Item(product=Product(id=2, name='Kubernetes', price=2.0, stock=98), quantity=1)
        ]

    def test_calculate_total(self):
        print("test_calculate_total")
        Checkout.calculate_total(self.cart_items)
        actual_result = Checkout._total_purchase
        self.assertEqual(actual_result, 3.0)

    @mock.patch(
        "infrastructure.file.file.UpdateStock.save_product_stock",
        return_value=[
            "1;Microservices;1.0;99;\n",
            "2;Kubernetes;2.0;99;\n",
            "3;Docker;3.0;99;\n",
            "4;Architecture;4.0;99;\n",
            "5;Communication;5.0;99;\n",
            "6;Observability;6.0;99;\n",
        ],
    )
    def test_adjust_stock(self, mock_open_file):
        print("test_adjust_stock")
        actual_result = read_lines()
        Checkout.adjust_stock(self.cart_items)
        expected_result = [
            "1;Microservices;1.0;98;\n",
            "2;Kubernetes;2.0;99;\n",
            "3;Docker;3.0;99;\n",
            "4;Architecture;4.0;99;\n",
            "5;Communication;5.0;99;\n",
            "6;Observability;6.0;99;\n",
        ]
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
