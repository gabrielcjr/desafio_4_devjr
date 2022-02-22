from products import SelectedProduct
import file
import outputs


class Cart:

    cart_item: list = []

    @staticmethod
    def cart(product: int, amount: int, products_list: dict):
        validated_choice: dict = SelectedProduct.selected_product(
            products_list, product, amount
        )
        Cart.cart_item.append(validated_choice)


class Purchase:

    __total_purchase: float = 0

    @staticmethod
    def purchase_result(purchase: str):
        if purchase == "n":
            outputs.CartPurchase.your_purchase()
            for index, itens in enumerate(Cart.cart_item):
                item = Cart.cart_item[index]
                Purchase.__total_purchase = item["subtotal_price"] + Purchase.__total_purchase
                file.UpdateInventory.save_product_inventory(item["product"], item["available_inventory"])
                outputs.CartPurchase.purchase_details(
                    item["name"], item["amount"], item["price"], item["subtotal_price"]
                )
            outputs.CartPurchase.total_purchase(Purchase.__total_purchase)
            exit(0)
        elif purchase == "s":
            outputs.CartPurchase.keep_purchase()
