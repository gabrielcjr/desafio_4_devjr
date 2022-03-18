from domain.entity.product import Product
from typing import List


class Collection:

    products: List[Product] = []

    products_list: dict = {}

    def load_products_list(list: List[Product]) -> None:
        for index, product in enumerate(list):
            Collection.add_products(
                list[index].id, list[index].name, list[index].price, list[index].stock
            )

    def add_products(id, name, price, stock) -> None:
        Collection.products_list[int(id)] = {
            "name": name,
            "price": float(price),
            "stock": int(stock),
        }
