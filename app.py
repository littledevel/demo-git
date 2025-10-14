from http import server

class Hello(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        with open("test.html", 'r') as htmlfile:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(htmlfile.read().encode())

def main():
    s = server.HTTPServer(("0.0.0.0", 80), Hello)
    s.serve_forever()
main()

