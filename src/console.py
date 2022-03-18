from domain.service.collection import Collection
from domain.service.inputs import Inputs
from domain.entity.cart import Cart
import domain.service.utils as utils
import domain.template.outputs_console as outputs_console
import infrastructure.file.file as file


def main():

    utils.utils.clear()

    outputs_console.Header.header()

    outputs_console.List.list_items()

    file.File.load_product_data()

    while True:

        # Iniciar o cart aqui
        cart = Cart()

        Collection.load_products_list(Collection.products)

        outputs_console.List.products_list(Collection.products_list)

        user_input_product: str = Inputs.input_product(
            outputs_console.InputsQuestions.which_product(), Collection.products_list
        )

        user_input_amount: str = Inputs.input_amount(
            outputs_console.InputsQuestions.which_amount()
        )

        user_input_keep_purchase: str = Inputs.input_keep_purchase(
            outputs_console.InputsQuestions.keep_purchase()
        )

        utils.utils.clear()

        cart.add_item(user_input_product, user_input_amount, Collection.products_list)

        outputs_console.CartPurchase.keep_purchase(
            user_input_keep_purchase, Collection.products_list
        )


main()
