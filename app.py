from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Python Backend (via Nginx)")

server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"Backend running on port {PORT}")
server.serve_forever()
