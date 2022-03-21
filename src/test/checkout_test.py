import unittest
from unittest import mock
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.service.checkout import Checkout


class TestInputs(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.cart_items: list = [
            {
                "product": 1,
                "name": "Microservices",
                "price": 1.0,
                "subtotal_price": 1.0,
                "amount": 1.0,
                "available_stock": 99,
            }
        ]

    def test_calculate_total(self):
        print("test_calculate_total")
        Checkout.calculate_total(self.cart_items)
        actual_result = Checkout._total_purchase
        self.assertEqual(actual_result, 1)

    @mock.patch("file.save_product_inventory", return_value=0)
    @mock.patch("cart.exit", return_value=0)
    def test_adjust_stock(self, mock_save_product_inventory, mock_exit):
        print("test_adjust_stock")
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        cart.purchase_result(self.purchase_no)
        sys.stdout = sys.__stdout__
        expected_result = "Esta é a sua compra. Obrigado por comprar com a Full Cycle Store!\n\n     Item: Microsserviços, quantidade 1, valor unitário 1.00, subtotal 1.00\n\nO valor total da compra: 1.00\n"
        self.assertEqual(capturedOutput.getvalue(), expected_result)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        cart.purchase_result(self.purchase_yes)
        sys.stdout = sys.__stdout__
        expected_result = "Selecione o produto conforme a lista abaixo\n"
        self.assertEqual(capturedOutput.getvalue(), expected_result)


if __name__ == "__main__":
    unittest.main()
