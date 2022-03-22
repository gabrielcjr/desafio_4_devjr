import unittest
from unittest import mock
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from infrastructure.file.file import File, BuildProductList, UpdateStock
from domain.service.collection import Collection

BASE_PATH = os.path.abspath(os.path.dirname(__file__))


def open_file(mode):
    return open(BASE_PATH + '/_stock_file.txt', mode)


def open_file2(mode):
    return open(BASE_PATH + '/_stock_file2.txt', mode)


def read_lines():
    file = open_file('r')
    lines = file.readlines()
    file.close()
    return lines


class TestFile(unittest.TestCase):

    def setUp(self):
        self.product_data = ['1', 'Microsserviços', '1.0', '99']
        self.product_line = '1;Microsserviços;1.0;99;'
        self.product = 1
        self.inventory = 98
        self.lines = ['1;Microsserviços;1.0;98;\n', '2;Kubernetes;2.0;99;\n', '3;Docker;3.0;99;\n', '4;Arquitetura;4.0;99;\n', '5;Comunicação;5.0;99;\n', '6;Observabilidade;6.0;99;\n']

    @mock.patch('infrastructure.file.file.File.open_file', return_value=open_file2('w'))
    def test_update_inventory(self, mock_open_file):
        print('test_update_inventory')
        UpdateStock._UpdateStock__update_stock(self.lines, 'w')
        expected_result = {1: {'name': 'Microsserviços', 'price': 1.0, 'inventory': 98}, 2: {'name': 'Kubernetes', 'price': 2.0, 'inventory': 99}, 3: {'name': 'Docker', 'price': 3.0, 'inventory': 99}, 4: {'name': 'Arquitetura', 'price': 4.0, 'inventory': 99}, 5: {'name': 'Comunicação', 'price': 5.0, 'inventory': 99}, 6: {'name': 'Observabilidade', 'price': 6.0, 'inventory': 99}}
        self.assertEqual(Collection.products_dict, expected_result)

    def test_add_product_list(self):
        print('test_add_product_list')
        file.add_product_list(self.product_data)
        expected_result = {1: {'name': 'Microsserviços', 'price': 1.0, 'inventory': 99}}
        self.assertEqual(products.products, expected_result)

    @mock.patch('file.add_product_list', return_value=['1', 'Microsserviços', '1.0', '99'])
    def test_extrac_products_list(self, mock_extrac_products_list):
        print('test_extrac_products_list')
        file.extrac_products_list(self.product_line)
        expected_result = {1: {'name': 'Microsserviços', 'price': 1.0, 'inventory': 99}}
        self.assertEqual(products.products, expected_result)

    def test_read_products_list(self):
        print('test_read_products_list')
        file1 = open_file('r')
        file.read_products_list(file1)
        file1.close()
        expected_result = {1: {'name': 'Microsserviços', 'price': 1.0, 'inventory': 98}, 2: {'name': 'Kubernetes', 'price': 2.0, 'inventory': 99}, 3: {'name': 'Docker', 'price': 3.0, 'inventory': 99}, 4: {'name': 'Arquitetura', 'price': 4.0, 'inventory': 99}, 5: {'name': 'Comunicação', 'price': 5.0, 'inventory': 99}, 6: {'name': 'Observabilidade', 'price': 6.0, 'inventory': 99}}
        self.assertEqual(products.products, expected_result)

    @mock.patch('file.open_file', return_value=open_file('r'))
    def test_load_product_data(self, mock_open_file):
        print('test_load_product_data')
        file.load_product_data()
        expected_result = {1: {'name': 'Microsserviços', 'price': 1.0, 'inventory': 98}, 2: {'name': 'Kubernetes', 'price': 2.0, 'inventory': 99}, 3: {'name': 'Docker', 'price': 3.0, 'inventory': 99}, 4: {'name': 'Arquitetura', 'price': 4.0, 'inventory': 99}, 5: {'name': 'Comunicação', 'price': 5.0, 'inventory': 99}, 6: {'name': 'Observabilidade', 'price': 6.0, 'inventory': 99}}
        self.assertEqual(products.products, expected_result)

    @mock.patch('file.update_inventory', return_value=['1;Microsserviços;1.0;98;\n', '2;Kubernetes;2.0;99;\n', '3;Docker;3.0;99;\n', '4;Arquitetura;4.0;99;\n', '5;Comunicação;5.0;99;\n', '6;Observabilidade;6.0;99;\n'])
    def test_save_product_inventory(self, mock_update_inventory):
        print('test_save_product_inventory')
        file.save_product_inventory(self.product, self.inventory)
        actual_result = read_lines()
        expected_result = ['1;Microsserviços;1.0;98;\n', '2;Kubernetes;2.0;99;\n', '3;Docker;3.0;99;\n', '4;Arquitetura;4.0;99;\n', '5;Comunicação;5.0;99;\n', '6;Observabilidade;6.0;99;\n']
        self.assertEqual(actual_result, expected_result)

    @mock.patch('file.open_file', return_value=open_file('r'))
    def test_read_lines(self, mock_open_file):
        print('test_read_lines')
        file.read_lines()
        expected_result = {1: {'name': 'Microsserviços', 'price': 1.0, 'inventory': 98}, 2: {'name': 'Kubernetes', 'price': 2.0, 'inventory': 99}, 3: {'name': 'Docker', 'price': 3.0, 'inventory': 99}, 4: {'name': 'Arquitetura', 'price': 4.0, 'inventory': 99}, 5: {'name': 'Comunicação', 'price': 5.0, 'inventory': 99}, 6: {'name': 'Observabilidade', 'price': 6.0, 'inventory': 99}}
        self.assertEqual(products.products, expected_result)


if __name__ == '__main__':
    unittest.main()
