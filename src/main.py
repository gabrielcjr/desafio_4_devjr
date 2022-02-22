from products import ProductsList
from inputs import Inputs
from cart import Cart, Purchase
import utils
import file
import outputs


def main():

    utils.utils.clear()

    outputs.Header.header()

    outputs.List.list()

    file.File.load_product_data()

    while True:

        ProductsList.products_list(ProductsList.products)

        user_input_product: str = Inputs.input_product(
            outputs.InputsQuestions.which_product(), ProductsList.products
        )

        user_input_amount: str = Inputs.input_amount(
            outputs.InputsQuestions.which_amount()
        )

        user_input_keep_purchase: str = Inputs.input_keep_purchase(
            outputs.InputsQuestions.keep_purchase()
        )

        utils.utils.clear()

        Cart.cart(user_input_product, user_input_amount, ProductsList.products)

        Purchase.purchase_result(user_input_keep_purchase)


main()
