import http.server
import socketserver


SERVER_IP = "127.0.0.8"
SERVER_PORT = 8088

def start_file_server():
    handler = http.server.SimpleHTTPRequestHandler
    server = socketserver.TCPServer((SERVER_IP, SERVER_PORT), handler)

    print("File server is running at http://{}:{}".format(SERVER_IP, SERVER_PORT))

    server.serve_forever()

start_file_server()


