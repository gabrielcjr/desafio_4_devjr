from domain.entity.item import Item
from domain.entity.product import Product
from domain.service.cart import cart
from domain.service.collection import Collection
from domain.service.inputs import Inputs
import domain.service.utils as utils
import domain.template.outputs_console as outputs_console
import infrastructure.file.file as file


def main():

    utils.utils.clear()

    outputs_console.Header.header()

    outputs_console.List.list_items()

    file.File.load_product_data()

    while True:

        Collection.load_products_list(Collection.products_list)

        outputs_console.List.products_list(Collection.products_dict)

        user_input_product: int = Inputs.input_product(
            outputs_console.InputsQuestions.which_product(), Collection.products_dict
        )

        user_input_quantity: int = Inputs.input_quantity(
            outputs_console.InputsQuestions.which_quantity()
        )

        user_input_keep_purchase: str = Inputs.input_keep_purchase(
            outputs_console.InputsQuestions.keep_purchase()
        )

        validated_choice: Product | None = Product(user_input_product, Collection.products_dict[user_input_product]['name'], Collection.products_dict[user_input_product]['price'], Collection.products_dict[user_input_product]['stock'])

        new_item = Item(validated_choice, user_input_quantity)

        cart.add_item(new_item)
        print(cart.items)

        outputs_console.CartPurchase.keep_purchase(user_input_keep_purchase, cart.items)


main()
