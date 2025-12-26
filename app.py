import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        now = datetime.utcnow().isoformat()

        response = f"""
Hello from Python App
---------------------
Hostname: {hostname}
Time (UTC): {now}
"""

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Server started on port 8000")
server.serve_forever()
