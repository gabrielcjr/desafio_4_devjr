from domain.entity.product import Product
from typing import List


class Collection:

    products_list: List[Product] = []

    products_dict: dict = {}

    @staticmethod
    def load_products_list(list: List[Product]) -> None:
        for index, product in enumerate(list):
            Collection.add_products(
                list[index].id, list[index].name, list[index].price, list[index].stock
            )

    @classmethod
    def add_products(self, id: int, name: str, price: float, stock: int) -> None:
        self.products_dict[int(id)] = {
            "name": name,
            "price": float(price),
            "stock": int(stock),
        }
