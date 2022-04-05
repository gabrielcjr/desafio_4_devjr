import unittest
from unittest import mock
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.service.inputs import Inputs


class TestInputs(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.input_product = 1
        self.input_amount = 1
        self.keep_purchase = "n"
        self.message = "\nQual produto você gostaria de comprar?\n"
        self.products = {
            1: {"name": "Microsserviços", "price": 1.0, "inventory": 99},
            2: {"name": "Kubernetes", "price": 2.0, "inventory": 99},
            3: {"name": "Docker", "price": 3.0, "inventory": 99},
            4: {"name": "Arquitetura", "price": 4.0, "inventory": 99},
            5: {"name": "Comunicação", "price": 5.0, "inventory": 99},
            6: {"name": "Observabilidade", "price": 6.0, "inventory": 99},
        }

    @mock.patch("domain.service.inputs.input", return_value="1")
    def test_select_product(self, mock_which_product):
        print("test_select_product")
        actual_result = Inputs.input_product(self.input_product, self.products)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    @mock.patch("domain.service.inputs.input", return_value="1")
    def test_select_amount(self, mock_which_amount):
        print("test_select_amount")
        actual_result = Inputs.input_quantity(self.input_amount)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    @mock.patch("domain.service.inputs.input", return_value="n")
    def test_input_decision(self, mock_which_option):
        print("test_input_decision")
        actual_result = Inputs.input_keep_purchase(self.keep_purchase)
        expected_result = "n"
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
