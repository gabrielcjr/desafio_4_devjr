from domain.service.utils import utils

class Header:
    @staticmethod
    def header() -> None:
        return print("################## Full Cycle Store ################## \n")


class List:
    @staticmethod
    def list_items() -> None:
        return print("Lista de produtos da loja \n")

    @staticmethod
    def products_list(items: list) -> None:
        list_products: str = ""
        for product in items:
            name: str = items[product]["name"]
            price: float = items[product]["price"]
            list_products += "%s - %s R$ %.2f\n" % (product, name, price)
        return print(list_products)


class InputsQuestions:
    @staticmethod
    def which_product():
        return "\nQual produto você gostaria de comprar?\n"

    @staticmethod
    def which_amount():
        return "Qual a quantidade deste produto deseja comprar? \n"

    @staticmethod
    def keep_purchase():
        return (
            "Você deseja continuar suas compras? Digite 's' para sim ou 'n' para não \n"
        )


class CartPurchase:
    @staticmethod
    def your_purchase():
        return print(
            "Esta é a sua compra. Obrigado por comprar com a Full Cycle Store!\n"
        )

    @staticmethod
    def purchase_details(name, amount, price, subtotal):
        return print(
            "     Item: %s, quantidade %.0f, valor unitário %.2f, subtotal %.2f"
            % (name, amount, price, subtotal)
        )

    @staticmethod
    def total_purchase(total):
        return print("\nO valor total da compra: %.2f" % (total))

    @staticmethod
    def keep_purchase_title():
        return print("Selecione o produto conforme a lista abaixo")
    
    @staticmethod
    def keep_purchase(value, cart):
        utils.clear()
        if value == 'n':
            from domain.service.checkout import Checkout
            CartPurchase.your_purchase()
            for item in cart:
                CartPurchase.purchase_details(item["name"], item["amount"], item["price"], item["subtotal_price"])
            Checkout.place_order()
            CartPurchase.total_purchase(Checkout._total_purchase)
            exit(0)
        else:
            CartPurchase.keep_purchase_title()


class InputsWarnings:
    @staticmethod
    def input_product():
        from service.collection import products
        return print(
            "Por favor, escolha o produto entre 1 e %s"
            % str(len(products))
        )

    @staticmethod
    def input_amount():
        return print("Por favor, escolha uma quantidade até 9 itens")

    @staticmethod
    def input_keep():
        return print("Por favor, digite s para sim e n para não")


class StockCheck:
    @staticmethod
    def stock_not_available():
        print("Não temos estoque suficiente para este produto.")