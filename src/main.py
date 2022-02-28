from products import ProductsList
from cart import Cart, Purchase
import file
import outputs
from http.server import HTTPServer, BaseHTTPRequestHandler
# from http import cookies
from random import seed

HOST = "0.0.0.0"
PORT = 8080

file.File.load_product_data()

# C = cookies.SimpleCookie()


class Server(BaseHTTPRequestHandler):

    def do_GET(self):

        ID = self.path[-1]

        def _response_header():
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()

        if self.path == '/':
            _response_header()
            self.wfile.write(bytes(outputs.List.list_products(), "utf-8"))

        if self.path == ('/cart/' + ID):
            Cart.cart(int(ID), 1, ProductsList.products)
            _response_header()
            self.wfile.write(bytes(outputs.CartPurchase.current_cart(), "utf-8"))

        if self.path == ('/cart'):
            _response_header()
            self.wfile.write(bytes("test", "utf-8"))

        if self.path == '/checkout/':
            Purchase.calculate_total()
            _response_header()
            self.wfile.write(bytes(outputs.Checkout.checkout(), "utf-8"))

        if self.path == '/success/':
            seed()
            Purchase.adjust_inventory()
            _response_header()
            Purchase._total_purchase = 0
            Cart.cart_item = []
            self.wfile.write(bytes(outputs.Success.success_msg(), "utf-8"))


server = HTTPServer((HOST, PORT), Server)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped")
