import unittest
from unittest import mock
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from domain.service.checkout import Checkout

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

def open_file(mode):
    return open(BASE_PATH + '/_test.txt', mode)


def open_file2(mode):
    return open(BASE_PATH + '/_stock_file2.txt', mode)


def read_lines():
    file = open_file('r')
    lines = file.readlines()
    file.close()
    return lines


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
                "available_stock": 98,
            },
            {
                "product": 2,
                "name": "Microservices",
                "price": 1.0,
                "subtotal_price": 1.0,
                "amount": 1.0,
                "available_stock": 98,
            }
        ]
        # self.product_data = ['1', 'Microsserviços', '1.0', '99']
        # self.product_line = '1;Microsserviços;1.0;99;'
        # self.product = 1
        # self.inventory = 98
        # self.lines = ['1;Microsserviços;1.0;98;\n', '2;Kubernetes;2.0;99;\n', '3;Docker;3.0;99;\n', '4;Arquitetura;4.0;99;\n', '5;Comunicação;5.0;99;\n', '6;Observabilidade;6.0;99;\n']


    def test_calculate_total(self):
        print("test_calculate_total")
        Checkout.calculate_total(self.cart_items)
        actual_result = Checkout._total_purchase
        self.assertEqual(actual_result, 1)

    # @mock.patch('infrastructure.file.file.File.open_file', return_value=open_file2('w'))
    # @mock.patch("infrastructure.file.file.UpdateStock.save_product_stock", return_value=['1;Microsserviços;1.0;98;\n', '2;Kubernetes;2.0;99;\n', '3;Docker;3.0;99;\n', '4;Arquitetura;4.0;99;\n', '5;Comunicação;5.0;99;\n', '6;Observabilidade;6.0;99;\n'])
    # @mock.patch("domain.template.outputs_console.exit", return_value=0)
    # def test_adjust_stock(self, mock_open_file, mock_save_product_inventory, mock_exit):
    #     print("test_adjust_stock")
        
    #     Checkout.adjust_stock(self.cart_items)



if __name__ == "__main__":
    unittest.main()
