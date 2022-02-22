import os
from typing import List
# from typing import Any
from products import ProductsList
# from abc import ABC, abstractmethod

# class IPersistence(ABC):

#     @abstractmethod
#     def add_product_list(self) -> Any: pass

#     @abstractmethod
#     def save_product_inventory(self) -> Any: pass


class File:

    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    print(BASE_PATH)

    def open_file(mode):
        return open(f'{File.BASE_PATH}/_store_file.txt', mode)

    @staticmethod
    def load_product_data():
        file = File.open_file("r")
        BuildProductList._read_products_list(file)
        file.close()

    def _read_lines(mode) -> List:
        file = File.open_file(mode)
        lines = file.readlines()
        file.close()
        return lines


class BuildProductList(File):

    def _read_products_list(file):
        lines = file.readlines()
        lines = lines[:]
        for product_line in lines:
            BuildProductList.__extract_products_list(product_line)

    def __extract_products_list(product_line):
        product_data = []
        product_line = product_line[:-2]
        product_data = list(product_line.split(";"))
        BuildProductList.__add_product_list(product_data)

    def __add_product_list(product_data):
        ProductsList.products[int(product_data[0])] = {
            "name": product_data[1],
            "price": float(product_data[2]),
            "inventory": int(product_data[3]),
        }


class UpdateInventory(File):

    @staticmethod
    def save_product_inventory(product, inventory):
        lines = File._read_lines('r')
        line = lines[product - 1]
        semicolon_pos_max = line.rfind(";") - 2
        new_line = line[:semicolon_pos_max] + str(inventory) + ";\n"
        lines[product - 1] = new_line
        UpdateInventory.__update_inventory(lines, 'w')

    def __update_inventory(change, mode):
        file = File.open_file(mode)
        file.writelines(change)
        file.close()
