
class Cart:

    #criar um tipo para manipular quantidade e o produto
    __items: list = []

    # def __init__(self, product: int = 0, amount: int = 0, products_list: dict = None):

    


    def add_item(product: int, amount: int, products_list: dict):
        from service.products import SelectedProduct
        validated_choice: dict = SelectedProduct.selected_product(
            products_list, product, amount
        )
        Cart.__items.append(validated_choice)


    def remove_item(value):
        item_to_remove = value - 1
        Cart.__items.pop(item_to_remove)

    @property
    def items(self):
        return self.__items
    







        
        
