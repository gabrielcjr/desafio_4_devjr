from products import ProductsList
from inputs import Inputs
from cart import Cart, Purchase
import utils
import file
import outputs_console


def main():

    utils.utils.clear()

    outputs_console.Header.header()

    outputs_console.List.list()

    file.File.load_product_data()

    while True:

        print(ProductsList.products_list(ProductsList.products))

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

        Purchase.keep_purchase(user_input_keep_purchase)


main()