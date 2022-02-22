import unittest
import os
import sys
import io

sys.path.append("src")
from products import ProductsList, SelectedProduct


class TestProducts(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.products = {
            1: {"name": "Microsserviços", "price": 1.0, "inventory": 99},
            2: {"name": "Kubernetes", "price": 2.0, "inventory": 99},
            3: {"name": "Docker", "price": 3.0, "inventory": 99},
            4: {"name": "Arquitetura", "price": 4.0, "inventory": 99},
            5: {"name": "Comunicação", "price": 5.0, "inventory": 99},
            6: {"name": "Observabilidade", "price": 6.0, "inventory": 99},
        }
        self.product_item = 1
        self.amount = 1
        self.item_inventory = 99
        self.products = {
            1: {"name": "Microsserviços", "price": 1.0, "inventory": 99},
            2: {"name": "Kubernetes", "price": 2.0, "inventory": 99},
            3: {"name": "Docker", "price": 3.0, "inventory": 99},
            4: {"name": "Arquitetura", "price": 4.0, "inventory": 99},
            5: {"name": "Comunicação", "price": 5.0, "inventory": 99},
            6: {"name": "Observabilidade", "price": 6.0, "inventory": 99},
        }

    def test_products_list(self):
        print("test_products_list")
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        ProductsList.products_list(self.products)
        sys.stdout = sys.__stdout__
        expected_result = "1 - Microsserviços R$ 1.00\n2 - Kubernetes R$ 2.00\n3 - Docker R$ 3.00\n4 - Arquitetura R$ 4.00\n5 - Comunicação R$ 5.00\n6 - Observabilidade R$ 6.00\n\n"
        self.assertEqual(capturedOutput.getvalue(), expected_result)

    def test_selected_product(self):
        print("test_selected_product")
        actual_result = SelectedProduct.selected_product(
            self.products, self.product_item, self.amount
        )
        expected_result = {
            "product": 1,
            "name": "Microsserviços",
            "price": 1.0,
            "subtotal_price": 1.0,
            "amount": 1.0,
            "available_inventory": 98,
        }
        self.assertEqual(actual_result, expected_result)

    def test_inventory_check(self):
        print("test_inventory_check")
        actual_result = SelectedProduct._SelectedProduct__inventory_check(
            self.amount, self.item_inventory
        )
        expected_result = True
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
