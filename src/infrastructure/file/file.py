import os
from typing import IO, Any, List
from domain.entity.product import Product


class ProductFileReader:

    BASE_PATH = os.path.abspath(os.path.dirname(__file__))

    
    def read(self, mode: str) -> List:
        file: IO = self.open_file(mode)
        lines: list = file.readlines()
        lines = lines[:] # 
        product = []
        for line in lines: #for ou if
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
        return Product(id, name, price, stock)

    @staticmethod
    def open_file(mode: str) -> IO:
        return open(f"{ProductFileReader.BASE_PATH}/_store_file.txt", mode)


    @staticmethod
    def load_lines() -> None:
        file: IO = ProductFileReader.open_file("r")
        lines: list = file.readlines()
        file.close()
        return lines

class UpdateStock():
    @staticmethod
    def save_product_stock(product: int, stock: int) -> None:
        lines: list = ProductFileReader.load_lines()
        line: str = lines[product - 1]
        semicolon_pos_max = line.rfind(";") - 2
        new_line = line[:semicolon_pos_max] + str(stock) + ";\n"
        lines[product - 1] = new_line
        UpdateStock.__update_stock(lines, "w")

    @classmethod
    def __update_stock(cls, change: List, mode: str) -> None:
        file = ProductFileReader.open_file(mode)
        file.writelines(change)
        file.close()
