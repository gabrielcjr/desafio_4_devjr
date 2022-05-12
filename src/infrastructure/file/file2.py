import os
from typing import IO, Any, List
from domain.service.collection import Collection
from domain.entity.product import Product
#domain service - class não guarda dados

class File: # ProductFileReader

    BASE_PATH = os.path.abspath(os.path.dirname(__file__))

    def read(self) -> List[Product]:
        file: IO = self.__open_file()
        lines: list = file.readlines()
        lines = lines[:] # verificar
        for line in lines: #for ou if
            product = self.__convert_to_product(line)
    
    def __open_file(self) -> IO:
        return open(f"{cls.BASE_PATH}/_store_file.txt", 'r')


    def __convert_to_product(self, line: str) -> Product:
        line = line[:-2]
        data = list(line.split(";"))
        id: int = int(data[0])
        name: str = data[1]
        price: float = float(data[2])
        stock: int = int(data[3])
        return Product(id, name, price, stock)

    @staticmethod
    def load_product_data() -> None:
        file: IO = File.open_file("r")
        BuildProductList._read_products_list(file)
        file.close()

    @classmethod
    def _read_lines(cls, mode: str) -> List:
        file: IO = cls.open_file(mode)
        lines: list = file.readlines()
        file.close()
        return lines

class ProductFileWriter:

    def write(self, product: Product):
        # encontrar a linha do produto no arquivo

# leio, transcrever de file para class Product
# escrevo, transcrever class Product para file


class BuildProductList(File):
    @staticmethod
    def _read_products_list(file_to_load: IO) -> None:
        lines: list = file_to_load.readlines()
        lines = lines[:]
        for product_line in lines:
            BuildProductList.__extract_products_list(product_line)

    @classmethod
    def __extract_products_list(cls, product_line: str) -> None:
        product_data = []
        product_line = product_line[:-2]
        product_data = list(product_line.split(";"))
        cls.__add_product_list(product_data)

    @classmethod
    def __add_product_list(cls, product_data: list) -> None:
        id: int = int(product_data[0])
        name: str = product_data[1]
        price: float = float(product_data[2])
        stock: int = int(product_data[3])
        Collection.products_list.append(Product(id, name, price, stock))  # type: ignore


class UpdateStock(File):
    @staticmethod
    def save_product_stock(product: int, stock: int) -> None:
        lines: list = File._read_lines("r")
        line: str = lines[product - 1]
        semicolon_pos_max = line.rfind(";") - 2
        new_line = line[:semicolon_pos_max] + str(stock) + ";\n"
        lines[product - 1] = new_line
        UpdateStock.__update_stock(lines, "w")

    @classmethod
    def __update_stock(cls, change: List, mode: str) -> None:
        file = File.open_file(mode)
        file.writelines(change)
        file.close()