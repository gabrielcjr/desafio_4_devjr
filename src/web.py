from products import ProductsList
from cart import Cart, Purchase
import file
import outputs_web
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies
from random import seed

HOST = "0.0.0.0"
PORT = 8080

file.File.load_product_data()


class Server(BaseHTTPRequestHandler):

    def do_GET(self):

        C = cookies.Morsel()

        ID = self.path[-1]

        def __response_header():
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()

        def __response_header_with_cookie():
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.send_header("Set-Cookie", C.OutputString())
            self.end_headers()

        def __create_cookie():
            return ''.join(str(item["product"]) + "," for item in Cart.items)

        def __get_cookies():
            get_cookie = cookies.SimpleCookie(self.headers.get('Cookie'))
            cart_items_raw = get_cookie["item"].value
            return __remove_last_comma(cart_items_raw).split(",")

        def __remove_last_comma(value):
            return value[:-1]

        if self.path == '/':
            __response_header()
            self.wfile.write(bytes(outputs_web.List.list_products(), "utf-8"))

        if self.path == ('/cart/' + ID):
            Cart.cart(int(ID), 1, ProductsList.products)
            cart_items_cookie = __create_cookie()
            C.set("item", cart_items_cookie, cart_items_cookie)
            __response_header_with_cookie()

            self.wfile.write(bytes(outputs_web.CartPurchase.current_cart(), "utf-8"))

        if self.path == ('/cart/'):
            __response_header()
            if Cart.items:
                self.wfile.write(bytes(outputs_web.CartPurchase.current_cart(), "utf-8"))
            else:
                cart_items = __get_cookies()
                for item in cart_items:
                    Cart.cart(int(item), 1, ProductsList.products)
                self.wfile.write(bytes(outputs_web.CartPurchase.current_cart(), "utf-8"))

        if self.path == '/checkout/':
            Purchase.calculate_total(Cart.items)
            __response_header()
            self.wfile.write(bytes(outputs_web.Checkout.checkout(), "utf-8"))

        if self.path == '/success/':
            seed()
            Purchase.adjust_stock(Cart.items)
            __response_header()
            Purchase._total_purchase = 0
            Cart.items = []
            self.wfile.write(bytes(outputs_web.Success.success_msg(), "utf-8"))


server = HTTPServer((HOST, PORT), Server)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped")
