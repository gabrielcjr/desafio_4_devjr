from urllib.parse import parse_qs, urlparse
from products import ProductsList, SelectedProduct
from inputs import Inputs
from cart import Cart, Purchase
import file
import outputs
from http.server import HTTPServer, BaseHTTPRequestHandler



HOST = "0.0.0.0"
PORT = 8000

file.File.load_product_data()
class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        ID = self.path[-1]
        
        if self.path == '/':
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            html = '<html><body>' + outputs.Header.header() + '<br>' + outputs.List.list() \
                + '<br>' + ProductsList.products_list(ProductsList.products)+ '</html></body>'
            self.wfile.write(bytes(html, "utf-8"))
        
        if self.path == ('/cart/' + ID):
            Cart.cart(int(ID), 1, ProductsList.products)
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            html = '<html><body>' + outputs.Header.header() + '<br>' + \
                Purchase.purchase_result() + \
                '<br><input type="button" value="Keep buying!" onclick="history.back()"><br>\
                <form action="http://localhost:8000/checkout/"><input type="submit" value="Checkout!">\
                </form></body></html>'
            self.wfile.write(bytes(html, "utf-8"))
        
        if self.path == '/checkout/?':
            self.send_response(200)
            self.send_header("Context-type", "text/html")
            self.end_headers()
            html = '<html><body>' + outputs.Header.header() + '<br>' + \
                outputs.CartPurchase.total_purchase(Purchase._total_purchase) + \
                '</body></html>'
            self.wfile.write(bytes(html, "utf-8"))
        


# def main():

#     outputs.Header.header()

#     outputs.List.list()

#     file.File.load_product_data()

#     while True:

#         ProductsList.products_list(ProductsList.products)

#         user_input_product: str = Inputs.input_product(
#             outputs.InputsQuestions.which_product(), ProductsList.products
#         )

#         user_input_amount: str = Inputs.input_amount(
#             outputs.InputsQuestions.which_amount()
#         )

#         user_input_keep_purchase: str = Inputs.input_keep_purchase(
#             outputs.InputsQuestions.keep_purchase()
#         )

#         Cart.cart(user_input_product, user_input_amount, ProductsList.products)

#         Purchase.purchase_result(user_input_keep_purchase)


# main()

server = HTTPServer((HOST, PORT), Server)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped")