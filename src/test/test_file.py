import unittest
from unittest import mock
import os
import sys
sys.path.append("src")
from file import UpdateInventory, BuildProductList, File
from products import ProductsList

BASE_PATH = os.path.abspath(os.path.dirname(__file__))


def open_file(mode):
    return open(f'{BASE_PATH}/_test.txt', mode)


def open_file2(mode):
    return open(f'{BASE_PATH}/_test2.txt', mode)


def read_lines():
    file = open_file("r")
    lines = file.readlines()
    file.close()
    return lines


class TestFile(unittest.TestCase):
    def setUp(self):
        self.product_data = ["1", "Microsserviços", "1.0", "99"]
        self.product_line = "1;Microsserviços;1.0;99;"
        self.product = 1
        self.inventory = 98
        self.lines = [
            "1;Microsserviços;1.0;98;\n",
            "2;Kubernetes;2.0;99;\n",
            "3;Docker;3.0;99;\n",
            "4;Arquitetura;4.0;99;\n",
            "5;Comunicação;5.0;99;\n",
            "6;Observabilidade;6.0;99;\n",
        ]

    @mock.patch("file.File.open_file", return_value=open_file("r"))
    def test_load_product_data(self, mock_open_file):
        print("test_load_product_data")
        File.load_product_data()
        expected_result = {
            1: {"name": "Microsserviços", "price": 1.0, "inventory": 98},
            2: {"name": "Kubernetes", "price": 2.0, "inventory": 99},
            3: {"name": "Docker", "price": 3.0, "inventory": 99},
            4: {"name": "Arquitetura", "price": 4.0, "inventory": 99},
            5: {"name": "Comunicação", "price": 5.0, "inventory": 99},
            6: {"name": "Observabilidade", "price": 6.0, "inventory": 99},
        }
        self.assertEqual(ProductsList.products, expected_result)

    def test_read_products_list(self):
        print("test_read_products_list")
        file1 = open_file("r")
        BuildProductList._read_products_list(file1)
        file1.close()
        expected_result = {
            1: {"name": "Microsserviços", "price": 1.0, "inventory": 98},
            2: {"name": "Kubernetes", "price": 2.0, "inventory": 99},
            3: {"name": "Docker", "price": 3.0, "inventory": 99},
            4: {"name": "Arquitetura", "price": 4.0, "inventory": 99},
            5: {"name": "Comunicação", "price": 5.0, "inventory": 99},
            6: {"name": "Observabilidade", "price": 6.0, "inventory": 99},
        }
        self.assertEqual(ProductsList.products, expected_result)

    @mock.patch(
        "file.BuildProductList._BuildProductList__add_product_list", return_value=["1", "Microsserviços", "1.0", "99"]
    )
    def test_extract_products_list(self, mock_extract_products_list):
        print("test_extract_products_list")
        BuildProductList._BuildProductList__extract_products_list(self.product_line)
        expected_result = {1: {"name": "Microsserviços", "price": 1.0, "inventory": 99}}
        self.assertEqual(ProductsList.products, expected_result)

    def test_add_product_list(self):
        print("test_add_product_list")
        BuildProductList._BuildProductList__add_product_list(self.product_data)
        expected_result = {1: {"name": "Microsserviços", "price": 1.0, "inventory": 99}}
        self.assertEqual(ProductsList.products, expected_result)

    @mock.patch("file.File.open_file", return_value=open_file("r"))
    def test_read_lines(self, mock_open_file):
        print("test_read_lines")
        File._read_lines('r')
        expected_result = {
            1: {"name": "Microsserviços", "price": 1.0, "inventory": 98},
            2: {"name": "Kubernetes", "price": 2.0, "inventory": 99},
            3: {"name": "Docker", "price": 3.0, "inventory": 99},
            4: {"name": "Arquitetura", "price": 4.0, "inventory": 99},
            5: {"name": "Comunicação", "price": 5.0, "inventory": 99},
            6: {"name": "Observabilidade", "price": 6.0, "inventory": 99},
        }
        self.assertEqual(ProductsList.products, expected_result)

    @mock.patch(
        "file.UpdateInventory._UpdateInventory__update_inventory",
        return_value=[
            "1;Microsserviços;1.0;98;\n",
            "2;Kubernetes;2.0;99;\n",
            "3;Docker;3.0;99;\n",
            "4;Arquitetura;4.0;99;\n",
            "5;Comunicação;5.0;99;\n",
            "6;Observabilidade;6.0;99;\n",
        ],
    )
    def test_save_product_inventory(self, mock_update_inventory):
        print("test_save_product_inventory")
        UpdateInventory.save_product_inventory(self.product, self.inventory)
        actual_result = read_lines()
        expected_result = [
            "1;Microsserviços;1.0;98;\n",
            "2;Kubernetes;2.0;99;\n",
            "3;Docker;3.0;99;\n",
            "4;Arquitetura;4.0;99;\n",
            "5;Comunicação;5.0;99;\n",
            "6;Observabilidade;6.0;99;\n",
        ]
        self.assertEqual(actual_result, expected_result)

    @mock.patch("file.File.open_file", return_value=open_file2("w"))
    def test_update_inventory(self, mock_open_file):
        print("test_update_inventory")
        UpdateInventory._UpdateInventory__update_inventory(self.lines, 'w')
        expected_result = {
            1: {"name": "Microsserviços", "price": 1.0, "inventory": 98},
            2: {"name": "Kubernetes", "price": 2.0, "inventory": 99},
            3: {"name": "Docker", "price": 3.0, "inventory": 99},
            4: {"name": "Arquitetura", "price": 4.0, "inventory": 99},
            5: {"name": "Comunicação", "price": 5.0, "inventory": 99},
            6: {"name": "Observabilidade", "price": 6.0, "inventory": 99},
        }
        self.assertEqual(ProductsList.products, expected_result)


if __name__ == "__main__":
    unittest.main()
