#!/usr/bin/python3
"""
...
"""

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleServer(BaseHTTPRequestHandler):
    """
    create a simple  HTTP server
    """
    def do_GET(self):
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

server_address = ("", 8000)
httpd = HTTPServer(server_address, SimpleServer)

httpd.serve_forever()
