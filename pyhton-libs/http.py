import SimpleHTTPServer
import socketserver

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("Serving at port %s" % PORT)
httpd.server_forever()