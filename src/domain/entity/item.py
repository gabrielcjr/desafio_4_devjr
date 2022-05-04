from dataclasses import dataclass

from domain.entity.product import Product


@dataclass
class Item:

    product: Product
    quantity: int

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    @property
    def get_product(self):
        return self.product

    @property
    def get_quantity(self):
        return self.quantity

    