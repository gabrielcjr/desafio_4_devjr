import os
from typing import IO, List
from domain.entity.product import Product


class ProductFileReader:

    BASE_PATH = os.path.abspath(os.path.dirname(__file__))

    def read(self, mode: str) -> List:
        file: IO = self.open_file(mode)
        lines: list = file.readlines()
        product = []
        for line in lines:  # for ou if
            product.append(self.__convert_to_product(line))
        file.close()
        return product

    def __convert_to_product(self, line: str) -> Product:
        line = line[:-2]
        data = list(line.split(";"))
        id: int = int(data[0])
        name: str = data[1]
        price: float = float(data[2])
        stock: int = int(data[3])
        return Product(id, name, price, stock)  # type: ignore

    @staticmethod
    def open_file(mode: str) -> IO:
        return open(f"{ProductFileReader.BASE_PATH}/_store_file.txt", mode)

    @staticmethod
    def load_lines() -> list:
        file: IO = ProductFileReader.open_file("r")
        lines: list = file.readlines()
        file.close()
        return lines


class ProductFileWriter():
    @staticmethod
    def write_product_file(product: int, new_value: int, field_to_change: int) -> None:
        lines: list = ProductFileReader.load_lines()
        line: str = lines[product - 1]
        line_to_change: list = line.split(';')
        for index, item in enumerate(line_to_change):
            if index == field_to_change:
                line_to_change[index] = str(new_value)
        new_line = ';'.join(line_to_change)
        lines[product - 1] = new_line
        ProductFileWriter.__update_file(lines, "w")

    @classmethod
    def __update_file(cls, change: List, mode: str) -> None:
        file = ProductFileReader.open_file(mode)
        file.writelines(change)
        file.close()
