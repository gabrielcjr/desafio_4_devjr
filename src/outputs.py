from random import randint


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
        from products import ProductsList
        html: str = '<html><body>' + Header.header() + '<br>' + List.list() + '<br>' + \
            ProductsList.products_list(ProductsList.products) + '<br>\
                <a href="http://localhost:8080/cart/">Cart</a>\
                    </body></html>'
        return html


class CartPurchase:

    @staticmethod
    def your_purchase():
        return "<br>This is your purchase. Thanks for buying at Full Cycle Store!<br>"

    @staticmethod
    def purchase_details(name, amount, price, subtotal):
        return "<br>     Item: %s, amount %.0f, unit price %.2f, subtotal %.2f <br>" % (name, amount, price, subtotal)

    @staticmethod
    def total_purchase(total):
        return "<br>This is the total of your purchase: %.2f <br>" % (total)

    @staticmethod
    def keep_purchase():
        return "<br>Select the product according to the list bellow <br>"

    @staticmethod
    def current_cart():
        from cart import Purchase
        html = '<html><body>' + Header.header() + '<br>' + Purchase.purchase_result() + \
            '<br><a href="http://localhost:8080/">Go back<a/><br> \
            <a href="http://localhost:8080/checkout/">Checkout</a> \
            </a></body></html>'
        return html


class Checkout:

    @staticmethod
    def checkout():
        from cart import Purchase
        html = '<html><body>' + Header.header() + '<br>' + \
            CartPurchase.total_purchase(Purchase._total_purchase) + \
            '<a href="http://localhost:8080/success/">Purchase</a>\
            </body></html>'
        return html


class Success:

    @staticmethod
    def success_msg():
        html = '<html><body>' + Header.header() + '<br>' + \
            'Congratulations! Your order number ' + str(randint(8000, 10000)) + ' has been placed successfully \
            </body></html>'
        return html


class InventoryCheck:
    @staticmethod
    def inventory_not_available():
        "<br>There is not enough itens available for this product.<br>"
