from products import ProductsList
from cart import Cart, Purchase
import file
import outputs
from http.server import HTTPServer, BaseHTTPRequestHandler
from random import seed

HOST = "0.0.0.0"
PORT = 8080

file.File.load_product_data()


class Server(BaseHTTPRequestHandler):

    def do_GET(self):

        ID = self.path[-1]

        if self.path == '/':
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(outputs.List.list_products(), "utf-8"))

        if self.path == ('/cart/' + ID):
            Cart.cart(int(ID), 1, ProductsList.products)
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(outputs.CartPurchase.current_cart(), "utf-8"))

        if self.path == '/checkout/?':
            Purchase.calculate_total()
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(outputs.Checkout.checkout(), "utf-8"))

        if self.path == '/success/?':
            seed()
            Purchase.adjust_inventory()
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            Purchase._total_purchase = 0
            Cart.cart_item = []
            self.wfile.write(bytes(outputs.Success.success_msg(), "utf-8"))


server = HTTPServer((HOST, PORT), Server)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped")
