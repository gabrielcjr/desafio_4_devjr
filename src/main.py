from operator import index
from products import ProductsList
from cart import Cart, Purchase
import file
import outputs
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies, cookiejar
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

        if self.path == '/':
            __response_header()
            self.wfile.write(bytes(outputs.List.list_products(), "utf-8"))

        if self.path == ('/cart/' + ID):
            cart_items = []
            Cart.cart(int(ID), 1, ProductsList.products)
            for item in Cart.cart_item:
                cart_items.append(item["product"])
            C.set("item", cart_items, cart_items)
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.send_header("Set-Cookie", C.OutputString())
            self.end_headers()
            self.wfile.write(bytes(outputs.CartPurchase.current_cart(), "utf-8"))

        if self.path == ('/cart/'):

            __response_header()
            saved_list = cookies.SimpleCookie(self.headers.get('Cookie'))
            print(saved_list)
            self.wfile.write(bytes("test", "utf-8"))

        if self.path == '/checkout/':
            Purchase.calculate_total()
            __response_header()
            self.wfile.write(bytes(outputs.Checkout.checkout(), "utf-8"))

        if self.path == '/success/':
            seed()
            Purchase.adjust_inventory()
            __response_header()
            Purchase._total_purchase = 0
            Cart.cart_item = []
            self.wfile.write(bytes(outputs.Success.success_msg(), "utf-8"))


server = HTTPServer((HOST, PORT), Server)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped")
