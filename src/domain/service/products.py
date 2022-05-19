from typing import Union


class SelectedProduct:

    __MINIMAL_STOCK_AVAILABILITY: int = 10

    @staticmethod
    def stock_check(input_quantity: int, item_stock: int) -> Union[bool, None]:
        stock: int = int(item_stock)
        if input_quantity <= (stock - SelectedProduct.__MINIMAL_STOCK_AVAILABILITY):
            return True
        from domain.template.outputs_console import StockCheck
        StockCheck.stock_not_available()
        exit(0)
