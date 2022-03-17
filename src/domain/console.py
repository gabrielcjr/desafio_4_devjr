from service.product import product
from service.products import ProductsList
from service.inputs import Inputs
from service.cart import cart
import service.utils as utils
import os
import sys
import template.outputs_console as outputs_console

currentdir = f'{os.path.dirname(os.path.realpath(__file__))}/../'
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import infrastructure.file.file as file



def main():

    utils.utils.clear()

    outputs_console.Header.header()

    outputs_console.List.list_items()

    file.File.load_product_data()


    while True:

        cart = Cart()

        outputs_console.List.products_list(product.get_products())

        user_input_product: str = Inputs.input_product(
            outputs_console.InputsQuestions.which_product(), product.get_products()
        )

        user_input_amount: str = Inputs.input_amount(
            outputs_console.InputsQuestions.which_amount()
        )

        user_input_keep_purchase: str = Inputs.input_keep_purchase(
            outputs_console.InputsQuestions.keep_purchase()
        )

        utils.utils.clear()

        cart.add_item(user_input_product, user_input_amount, product.get_products())

        outputs_console.CartPurchase.keep_purchase(user_input_keep_purchase, cart.get_cart_items())


main()