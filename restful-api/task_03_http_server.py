#!/usr/bin/python3
"""
task_03_http_server.py
A simple API using Python's built-in http.server module.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for our simple API."""

    def _send_text(self, status_code: int, message: str) -> None:
        """Send a plain text response."""
        body = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status_code: int, payload: dict) -> None:
        """Send a JSON response."""
        body_str = json.dumps(payload)
        body = body_str.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
            return

        if self.path == "/status":
            self._send_text(200, "OK")
            return

        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, data)
            return

        if self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_json(200, info)
            return

        # Undefined endpoint
        self._send_text(404, "Endpoint not found")

    # Make server output cleaner (optional)
    def log_message(self, format, *args):
        return


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("\nServer stopped.")



if __name__ == "__main__":
    run()
