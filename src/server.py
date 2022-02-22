from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8000


class Store(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Context-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        msg = 'Hi there'
        self.wfile.write(bytes(msg, "utf-8"))


server = HTTPServer((HOST, PORT), Store)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped")