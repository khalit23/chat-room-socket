import socket
import threading

PORT = 5050
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)
FORMAT = "utf-8"

def handle_client(client_socket: socket.socket, client_address: tuple):
    byte_message = client_socket.recv(1024)
    msg = byte_message.decode(FORMAT)
    print(f"client: {client_address} has sent the message: {msg}")

def start_server(address: tuple):
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind(address)
    server.listen()
    print(f"[SERVER] is listening ...")
    while True:
        client_socket, client_address = server.accept()
        print(f"client: {client_address} has joined")
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        print(f"Active number of clients is: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server(ADDRESS)
