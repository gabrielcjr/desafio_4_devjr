from service.products import ProductsList
from service.inputs import Inputs
from entity.cart import Cart, Purchase
import service.utils as utils
import service.file as file
import template.outputs_console as outputs_console


def main():

    utils.utils.clear()

    outputs_console.Header.header()

    outputs_console.List.list_items()

    file.File.load_product_data()

    while True:
        
        outputs_console.List.products_list(ProductsList.products)

        user_input_product: str = Inputs.input_product(
            outputs_console.InputsQuestions.which_product(), ProductsList.products
        )

        user_input_amount: str = Inputs.input_amount(
            outputs_console.InputsQuestions.which_amount()
        )

        user_input_keep_purchase: str = Inputs.input_keep_purchase(
            outputs_console.InputsQuestions.keep_purchase()
        )

        utils.utils.clear()

        Cart.cart(user_input_product, user_input_amount, ProductsList.products)

        outputs_console.CartPurchase.keep_purchase(user_input_keep_purchase, Cart.items)


main()