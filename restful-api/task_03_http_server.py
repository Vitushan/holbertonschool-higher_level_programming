#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


from http.server import BaseHTTPRequestHandler
import socketserver



PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

with socketserver.TCPserver(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()