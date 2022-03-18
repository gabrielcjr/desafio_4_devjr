class Product:

    id: int
    name: str
    price: float
    stock: int

    def __init__(self, id: int, name: str, price: float, stock: int = 0) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def increment_stock(self, value):
        self.stock = self.stock + value

    def decrement_stock(self, value):
        new_stock = self.stock - value
        if new_stock < 0:
            raise Exception("Stock must be greater or equal than 0")
        self.stock = self.stock - value
