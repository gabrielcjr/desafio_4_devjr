import unittest
import sys
import os

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
        self.amount = 1
        self.item_stock = 99
        self.products = {
            1: {"name": "Microservices", "price": 1.0, "stock": 99},
            2: {"name": "Kubernetes", "price": 2.0, "stock": 99},
            3: {"name": "Docker", "price": 3.0, "stock": 99},
            4: {"name": "Architecture", "price": 4.0, "stock": 99},
            5: {"name": "Communication", "price": 5.0, "stock": 99},
            6: {"name": "Observability", "price": 6.0, "stock": 99},
        }

    # def test_selected_product(self):
    #     print("test_selected_product")
    #     actual_result = SelectedProduct.selected_product(
    #         self.products, self.product_item, self.amount
    #     )
    #     expected_result = {
    #         "product": 1,
    #         "name": "Microservices",
    #         "price": 1.0,
    #         "subtotal_price": 1.0,
    #         "amount": 1.0,
    #         "available_stock": 98,
    #     }
    #     self.assertEqual(actual_result, expected_result)

    # def test_stock_check(self):
    #     print("test_stock_check")
    #     actual_result = SelectedProduct._SelectedProduct__stock_check(
    #         self.amount, self.item_stock
    #     )
    #     expected_result = True
    #     self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
