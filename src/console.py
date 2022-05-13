from domain.entity.item import Item
from domain.entity.product import Product
from domain.service.cart import cart
from domain.service.inputs import Inputs
import domain.service.utils as utils
import domain.template.outputs_console as outputs_console
import infrastructure.file.file as file


def main():

    utils.utils.clear()

    outputs_console.Header.header()

    outputs_console.List.list_items()

    reader = file.ProductFileReader()

    all_products = reader.read("r")


    while True:

        outputs_console.List.products_list(all_products)

        user_input_product: int = Inputs.input_product(
            outputs_console.InputsQuestions.which_product(), all_products
        )

        user_input_quantity: int = Inputs.input_quantity(
            outputs_console.InputsQuestions.which_quantity()
        )

        user_input_keep_purchase: str = Inputs.input_keep_purchase(
            outputs_console.InputsQuestions.keep_purchase()
        )

        validated_choice: Product | None = Product(
            user_input_product, 
            all_products[user_input_product - 1].get_name, 
            all_products[user_input_product - 1].get_price, 
            all_products[user_input_product - 1].get_stock
            )

        new_item = Item(validated_choice, user_input_quantity)

        cart.add_item(new_item)

        outputs_console.CartPurchase.keep_purchase(user_input_keep_purchase, cart.items)


main()
