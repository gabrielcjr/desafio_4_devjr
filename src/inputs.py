import re
from typing import Union
import outputs_console


class Inputs:
    @staticmethod
    def input_product(message: str, products_list: dict) -> Union[int, None]:
        product_input: str = ""
        while type(product_input) != int:
            product_input = input(message)
            all_products: str = str(len(products_list))
            if re.match("^[1-" + str(all_products) + "]$", product_input):
                return int(product_input)
            else:
                outputs_console.InputsWarnings.input_product()

    @staticmethod
    def input_amount(message: str) -> Union[float, None]:
        amount_input: str = ""
        while type(amount_input) != float:
            amount_input = input(message)
            if re.match("^[1-9]$", amount_input):
                return float(amount_input)
            else:
                outputs_console.InputsWarnings.input_amount()

    @staticmethod
    def input_keep_purchase(message: str) -> Union[str, None]:
        input_option: str = ""
        while input_option != ["n", "s"]:
            input_option = input(message)
            if input_option in ["n", "s"]:
                return input_option
            else:
                outputs_console.InputsWarnings.input_keep()