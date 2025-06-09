#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


from http.server import BaseHTTPRequestHandler
import json
import socketserver


PORT = 8000


class Myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200, 'ok')
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_error(404, 'Endpoint not found')
            self.send_header("Content-Type", "text/plain")
            self.end_headers()


PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Myhandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
