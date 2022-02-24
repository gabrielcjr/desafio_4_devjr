from http.server import BaseHTTPRequestHandler
from outputs import Header, List

class Server(BaseHTTPRequestHandler):

    # def __init__(self, message):
    #     self.message = message



    # def do_POST(self):
    #     self.send_response(200)
    #     self.send_header("Content-type", "application/json")
    #     self.end_headers()

    #     msg = 'Hi there'
    #     self.wfile.write(bytes(msg, "utf-8"))

