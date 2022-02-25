from products import ProductsList, SelectedProduct
from cart import Cart, Purchase
import file
import outputs
from http.server import HTTPServer, BaseHTTPRequestHandler

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
            html = '<html><body>' + outputs.Header.header() + '<br>' + outputs.List.list() \
                + '<br>' + ProductsList.products_list(ProductsList.products) + '</html></body>'
            self.wfile.write(bytes(html, "utf-8"))

        if self.path == ('/cart/' + ID):
            Cart.cart(int(ID), 1, ProductsList.products)
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            html = '<html><body>' + outputs.Header.header() + '<br>' + \
                Purchase.purchase_result() + \
                '<br><input type="button" value="Keep buying!" onclick="history.back()"><br>\
                <form action="http://localhost:8080/checkout/"><input type="submit" value="Checkout!">\
                </form></body></html>'
            self.wfile.write(bytes(html, "utf-8"))

        if self.path == '/checkout/?':
            Purchase.calculate_total()
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            html = '<html><body>' + outputs.Header.header() + '<br>' + \
                outputs.CartPurchase.total_purchase(Purchase._total_purchase) + \
                '<form action="http://localhost:8080/success/"><input type="submit" value="Purchase!">\
                </body></html>'
            self.wfile.write(bytes(html, "utf-8"))

        if self.path == '/success/?':
            Purchase.adjust_inventory()
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            html = '<html><body>' + outputs.Header.header() + '<br>' + \
                'Congratulations! Your order has been placed \
                </body></html>'
            self.wfile.write(bytes(html, "utf-8"))


server = HTTPServer((HOST, PORT), Server)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped")
