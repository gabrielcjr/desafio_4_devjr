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

    _total_purchase: float = 0

    @staticmethod
    def purchase_result():
        result = ''
        for index, itens in enumerate(Cart.cart_item):
            item = Cart.cart_item[index]
            result += outputs.CartPurchase.purchase_details(
                item["name"], item["amount"], item["price"], item["subtotal_price"]
            )
        return result

    @staticmethod
    def calculate_total():
        for index, itens in enumerate(Cart.cart_item):
            item = Cart.cart_item[index]
            Purchase._total_purchase += item["subtotal_price"]

    @staticmethod
    def adjust_inventory():
        for index, itens in enumerate(Cart.cart_item):
            item = Cart.cart_item[index]
            file.UpdateInventory.save_product_inventory(item["product"], item["available_inventory"])
