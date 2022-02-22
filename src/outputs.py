class Header:
    @staticmethod
    def header() -> None:
        return print("################## Full Cycle Store ################## \n")


class List:
    @staticmethod
    def list() -> None:
        return print("Lista de produtos da loja \n")


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
    def keep_purchase():
        return print("Selecione o produto conforme a lista abaixo")


class InputsWarnings:
    @staticmethod
    def input_product():
        from products import ProductsList

        return print(
            "Por favor, escolha o produto entre 1 e %s"
            % str(len(ProductsList.products))
        )

    @staticmethod
    def input_amount():
        return print("Por favor, escolha uma quantidade até 9 itens")

    @staticmethod
    def input_keep():
        return print("Por favor, digite s para sim e n para não")


class InventoryCheck:
    @staticmethod
    def inventory_not_available():
        print("Não temos estoque suficiente para este produto.")
