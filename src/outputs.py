class Header:
    @staticmethod
    def header() -> None:
        return "################## Full Cycle Store ################## \n"


class List:
    @staticmethod
    def list() -> None:
        return "Store\'s Products List \n"


class InputsQuestions:
    @staticmethod
    def which_product():
        return "\Which product would you like to buy?\n"

    @staticmethod
    def which_amount():
        return "Which amount would you like to get? \n"

    @staticmethod
    def keep_purchase():
        return (
            "Do you want to keep the purchase? Select 's' to Yes or 'n' to No \n"
        )


class CartPurchase:
    @staticmethod
    def your_purchase():
        return "This is your purchase. Thanks for buying at Full Cycle Store!\n"

    @staticmethod
    def purchase_details(name, amount, price, subtotal):
        return "     Item: %s, amount %.0f, unit price %.2f, subtotal %.2f" % (name, amount, price, subtotal)
        

    @staticmethod
    def total_purchase(total):
        return "\nThis is the total of your purchase: %.2f" % (total)

    @staticmethod
    def keep_purchase():
        return "Select the product according to the list bellow"


class InputsWarnings:
    @staticmethod
    def input_product():
        from products import ProductsList
        return "Please, select the product between 1 and %s" % str(len(ProductsList.products))

    @staticmethod
    def input_amount():
        return "Max purchase of 9 itens. Please, select a lower quantity"

    @staticmethod
    def input_keep():
        return "PLease, type s to Yes or n to No"


class InventoryCheck:
    @staticmethod
    def inventory_not_available():
        "There is not enough itens available for this product."
