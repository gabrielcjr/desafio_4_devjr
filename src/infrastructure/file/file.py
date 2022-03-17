import os
from typing import Any, List
from domain.service.collection import Collection
from domain.entity.product import Product

class File:

    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    print(BASE_PATH)

    def open_file(mode):
        return open(f'{File.BASE_PATH}/_store_file.txt', mode)

    @staticmethod
    def load_product_data() -> Any:
        file = File.open_file("r")
        BuildProductList._read_products_list(file)
        file.close()

    def _read_lines(mode) -> List:
        file = File.open_file(mode)
        lines = file.readlines()
        file.close()
        return lines


# leio, transcrever de file para class Product
# escrevo, transcrever class Product para file


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
        id = int(product_data[0])
        name = product_data[1]
        price = float(product_data[2])
        stock = int(product_data[3])
        Collection.products.append(Product(id, name, price, stock))


class UpdateStock(File):

    @staticmethod
    def save_product_stock(product, stock):
        lines = File._read_lines('r')
        line = lines[product - 1]
        semicolon_pos_max = line.rfind(";") - 2
        new_line = line[:semicolon_pos_max] + str(stock) + ";\n"
        lines[product - 1] = new_line
        UpdateStock.__update_stock(lines, 'w')

    def __update_stock(change, mode):
        file = File.open_file(mode)
        file.writelines(change)
        file.close()
