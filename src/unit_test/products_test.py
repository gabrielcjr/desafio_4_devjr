import unittest
import sys
import os
from unittest import mock

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.service.products import SelectedProduct


class TestProducts(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.products = {
            1: {"name": "Microservices", "price": 1.0, "stock": 99},
            2: {"name": "Kubernetes", "price": 2.0, "stock": 99},
            3: {"name": "Docker", "price": 3.0, "stock": 99},
            4: {"name": "Architecture", "price": 4.0, "stock": 99},
            5: {"name": "Communication", "price": 5.0, "stock": 99},
            6: {"name": "Observability", "price": 6.0, "stock": 99},
        }
        self.product_item = 1
        self.valid_amount = 1
        self.invalid_amount = 99
        self.item_stock = 99
        self.products = {
            1: {"name": "Microservices", "price": 1.0, "stock": 99},
            2: {"name": "Kubernetes", "price": 2.0, "stock": 99},
            3: {"name": "Docker", "price": 3.0, "stock": 99},
            4: {"name": "Architecture", "price": 4.0, "stock": 99},
            5: {"name": "Communication", "price": 5.0, "stock": 99},
            6: {"name": "Observability", "price": 6.0, "stock": 99},
        }

    # @mock.patch("sys.exit(0)", return_value='')
    def test_stock_check(self):
        print("test_stock_check")
        actual_result = SelectedProduct.stock_check(
            self.valid_amount, self.item_stock
        )
        expected_result = True
        self.assertEqual(actual_result, expected_result)

        with self.assertRaises(SystemExit):
            actual_result = SelectedProduct.stock_check(self.invalid_amount, self.item_stock)

        self.assertEqual(SelectedProduct._SelectedProduct__MINIMAL_STOCK_AVAILABILITY, 10)


if __name__ == "__main__":
    unittest.main()
