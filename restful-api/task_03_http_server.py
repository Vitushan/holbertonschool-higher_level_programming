#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json




class Myhandler(BaseHTTPRequestHandler):
    """
    this is a subclass for get
    """
    def do_GET(self):
        """
        method do_get
        """
        if self.path == '/':
            self.send_response(200)
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

        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            error = {'error': '404 Not Found'}
            self.wfile.write(json.dumps(error).encode('utf-8'))
        


PORT = 8000
with HTTPServer(("", PORT), Myhandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
