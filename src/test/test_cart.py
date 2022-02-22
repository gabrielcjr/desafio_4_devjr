import unittest
from unittest import mock
import os
import io
import sys

sys.path.append("src")
from cart import Cart, Purchase


class TestChoice(unittest.TestCase):
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
        self.purchase_no = "n"
        self.purchase_yes = "s"
        self.cart_item = [
            {
                "product": 1,
                "name": "Microsserviços",
                "price": 1.0,
                "subtotal_price": 1.0,
                "amount": 1.0,
                "available_inventory": 98,
            }
        ]

    def test_cart(self):
        print("test_cart")
        Cart.cart(self.product_item, self.amount, self.products)
        expected_result = [
            {
                "product": 1,
                "name": "Microsserviços",
                "price": 1.0,
                "subtotal_price": 1.0,
                "amount": 1.0,
                "available_inventory": 98,
            }
        ]
        self.assertEqual(self.cart_item, expected_result)

    @mock.patch('file.UpdateInventory.save_product_inventory', return_value=0)
    @mock.patch('cart.exit', return_value=0)
    def test_purchase_result(self, mock_save_product_inventory, mock_exit):
        print('test_purchase_result')
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        Purchase.purchase_result(self.purchase_no)
        sys.stdout = sys.__stdout__
        expected_result = 'Esta é a sua compra. Obrigado por comprar com a Full Cycle Store!\n\n     Item: Microsserviços, quantidade 1, valor unitário 1.00, subtotal 1.00\n\nO valor total da compra: 1.00\n'
        self.assertEqual(capturedOutput.getvalue(), expected_result)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        Purchase.purchase_result(self.purchase_yes)
        sys.stdout = sys.__stdout__
        expected_result = 'Selecione o produto conforme a lista abaixo\n'
        self.assertEqual(capturedOutput.getvalue(), expected_result)


if __name__ == "__main__":
    unittest.main()
