import unittest
from unittest import mock
import io
import sys

sys.path.append("src")
from inputs import Inputs


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

    @mock.patch("inputs.input", return_value="1")
    def test_select_product(self, mock_which_product):
        print("test_select_product")
        actual_result = Inputs.input_product(self.input_product, self.products)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    # @mock.patch('inputs.input', return_value='100')
    # def test_select_product2(self, mock_which_product):
    #     print('test_select_product2')
    #     capturedOutput = io.StringIO()
    #     sys.stdout = capturedOutput
    #     inputs.input_product(self.input_product, self.products)
    #     sys.stdout = sys.__stdout__
    #     expected_result = 'Por favor, escolha o produto entre 1 e 6'
    #     self.assertEqual(capturedOutput.getvalue(), expected_result)

    @mock.patch("inputs.input", return_value="1")
    def test_select_amount(self, mock_which_amount):
        print("test_select_amount")
        actual_result = Inputs.input_amount(self.input_amount)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    @mock.patch("inputs.input", return_value="n")
    def test_input_decision(self, mock_which_option):
        print("test_input_decision")
        actual_result = Inputs.input_keep_purchase(self.keep_purchase)
        expected_result = "n"
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
