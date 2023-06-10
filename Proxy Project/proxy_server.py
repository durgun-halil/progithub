import socket
from cryptography.fernet import Fernet

private_key = Fernet.generate_key()
encryption_engine = Fernet(private_key)


def send_data(client_socket, data):
    client_socket.sendall(data.encode())

def authenticate_user(client_socket):
    username = client_socket.recv(1024).decode()
    password = client_socket.recv(1024).decode()

    if username == "manager" and password == "password":
        send_data(client_socket, "Authentication successful. Access granted.")
        return True
    else:
        send_data(client_socket, "Authentication failed. Access denied")
        return False


def handle_file_request(client_socket):
    file_name = client_socket.recv(1024).decode()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8088))

    server_socket.sendall(file_name.encode())

    file_data = server_socket.recv(1024)
    while file_data:
        encrypted_data = encryption_engine.encrypt(file_data)
        client_socket.sendall(encrypted_data)
        file_data = server_socket.recv(1024)

    server_socket.close()
    client_socket.close()



def initialize_proxy_server():
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind(('localhost', 8888))
    proxy_socket.listen(5)

    print("Server is running and Proxy is active")

    while True:
        client_socket, client_address = proxy_socket.accept()
        print("Client connection established:", client_address)

        if authenticate_user(client_socket):
            handle_file_request(client_socket)

initialize_proxy_server()
