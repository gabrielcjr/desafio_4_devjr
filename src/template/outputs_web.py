from random import randint

from entity.cart import Cart


class Header:
    @staticmethod
    def header() -> str:
        return "<br>################## Full Cycle Store ################## <br>"


class List:
    @staticmethod
    def list() -> str:
        return "<br>Store\'s Products List <br><br> Select bellow a product of your choice<br>"

    @staticmethod
    def list_products() -> str:
        from service.products import ProductsList
        return (
            (
                f'<html><body>{Header.header()}<br>{List.list()}<br>'
                + List.products_list(ProductsList.products)
            )
            + '<br>\
                <a href="http://localhost:8080/cart/">Cart</a>\
                    </body></html>'
        )
    
    @staticmethod
    def products_list(dict: dict):
        list_products: str = ""
        for product in dict:
            name: str = dict[product]["name"]
            price: float = dict[product]["price"]
            list_products += "<a href=\"cart\%s\">%s - %s $ %.2f</a><br>" % (product, product, name, price)
        return list_products
        


class CartPurchase:

    @staticmethod
    def your_purchase():
        return "<br>This is your purchase. Thanks for buying at Full Cycle Store!<br>"

    @staticmethod
    def purchase_details(value):
        result = ''
        for index, item in enumerate(value):
            item = value[index]
            result += "<br>     Item: %s, amount %.0f, unit price %.2f, subtotal %.2f <br>" % (item["name"], item["amount"], item["price"], item["subtotal_price"])
        return result

    @staticmethod
    def total_purchase(total):
        return "<br>This is the total of your purchase: %.2f <br>" % (total)

    @staticmethod
    def keep_purchase():
        return "<br>Select the product according to the list bellow <br>"

    @staticmethod
    def current_cart():
        from entity.cart import Purchase

        return (
            f'<html><body>{Header.header()}<br>{CartPurchase.purchase_details(Cart.items)}'
            + '<br><a href="http://localhost:8080/">Go back<a/><br> \
            <a href="http://localhost:8080/checkout/">Checkout</a> \
            </a></body></html>'
        )


class Checkout:

    @staticmethod
    def checkout():
        from entity.cart import Purchase
        return (
            (
                f'<html><body>{Header.header()}<br>'
                + CartPurchase.total_purchase(Purchase._total_purchase)
            )
            + '<a href="http://localhost:8080/success/">Purchase</a>\
            </body></html>'
        )
        


class Success:

    @staticmethod
    def success_msg():
        return (
            (
                f'<html><body>{Header.header()}<br>'
                + 'Congratulations! Your order number '
            )
            + str(randint(8000, 10000))
            + ' has been placed successfully \
            </body></html>'
        )
        


class StockCheck:
    @staticmethod
    def stock_not_available():
        "<br>There is not enough itens available for this product.<br>"
