import re
import domain.template.outputs_console as outputs_console


class Inputs:
    @staticmethod
    def input_product(message: str, products_list: dict) -> int | None:
        product_input: str = ""
        while type(product_input) != int:
            product_input = input(message)
            all_products: str = str(len(products_list))
            if re.match("^[1-" + str(all_products) + "]$", product_input):
                return int(product_input)
            else:
                outputs_console.InputsWarnings.input_product()

    @staticmethod
    def input_quantity(message: str) -> int | None:
        quantity_input: str = ""
        while type(quantity_input) != float:
            quantity_input = input(message)
            if re.match("^[1-9]$", quantity_input):
                return int(quantity_input)
            else:
                outputs_console.InputsWarnings.input_quantity()

    @staticmethod
    def input_keep_purchase(message: str) -> str | None:
        input_option: str = ""
        while input_option != ["n", "s"]:
            input_option = input(message)
            if input_option in ["n", "s"]:
                return input_option
            else:
                outputs_console.InputsWarnings.input_keep()
