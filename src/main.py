from operator import index
from products import ProductsList
from cart import Cart, Purchase
import file
import outputs
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
        
        def __get_cookies():
            get_cookie = cookies.SimpleCookie(self.headers.get('Cookie'))
            get_cart_items = get_cookie["item"].value
            last_comma_removed = get_cart_items[:-1]
            cart_items = last_comma_removed.split(",")
            return cart_items

        if self.path == '/':
            __response_header()
            self.wfile.write(bytes(outputs.List.list_products(), "utf-8"))

        if self.path == ('/cart/' + ID):
            cart_items_cookie = ''
            Cart.cart(int(ID), 1, ProductsList.products)
            for item in Cart.cart_item:
                cart_items_cookie += str(item["product"]) + ","
            C.set("item", cart_items_cookie, cart_items_cookie)
            __response_header_with_cookie()

            self.wfile.write(bytes(outputs.CartPurchase.current_cart(), "utf-8"))

        if self.path == ('/cart/'):
            __response_header()

            if Cart.cart_item:
                self.wfile.write(bytes(outputs.CartPurchase.current_cart(), "utf-8"))
            else:
                cart_items = __get_cookies()
                for item in cart_items:
                    Cart.cart(int(item), 1, ProductsList.products)
                self.wfile.write(bytes(outputs.CartPurchase.current_cart(), "utf-8"))

        if self.path == '/checkout/':
            Purchase.calculate_total()

            __response_header()
            self.wfile.write(bytes(outputs.Checkout.checkout(), "utf-8"))

        if self.path == '/success/':
            seed()
            C.set("item", "", "")
            Purchase.adjust_inventory()
            __response_header_with_cookie()
            Purchase._total_purchase = 0
            Cart.cart_item = []
            self.wfile.write(bytes(outputs.Success.success_msg(), "utf-8"))


server = HTTPServer((HOST, PORT), Server)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped")
