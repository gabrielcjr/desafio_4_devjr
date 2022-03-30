from dataclasses import dataclass

@dataclass
class Product:

    id: int
    name: str
    price: float
    stock: int

    def increment_stock(self, value):
        self.stock = self.stock + value

    def decrement_stock(self, value):
        new_stock = self.stock - value
        if new_stock < 0:
            raise Exception("Stock must be greater or equal than 0")
        self.stock = self.stock - value
