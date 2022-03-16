class Cart:

    __items: list = []

    product: int
    amount: int
    products_list: dict

    def __init__(self, product: int = 0, amount: int = 0, products_list: dict = None):
        self.product = product
        self.amount = amount
        self.products_list = products_list
    

    @staticmethod
    def add_item(product: int, amount: int, products_list: dict):
        from service.products import SelectedProduct
        validated_choice: dict = SelectedProduct.selected_product(
            products_list, product, amount
        )
        Cart.__items.append(validated_choice)


    @staticmethod
    def remove_item(value):
        item_to_remove = value - 1
        Cart.__items.pop(item_to_remove)


    def cart_items(self):
        return self.__items





        
        
