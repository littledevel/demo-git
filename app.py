from http import server

class Hello(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello from codehub\n".encode())

def main():
    s = server.HTTPServer(("0.0.0.0", 80), Hello)
    s.serve_forever()
main()

