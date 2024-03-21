import socket
import threading

PORT = 5050
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)
FORMAT = "utf-8"
SERVER = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

clients_addresses = []
client_sockets = []
address_to_name_translation = {}

def client_introduction(client_socket: socket.socket, client_address: tuple):
    client_name = client_socket.recv(1024).decode(FORMAT)
    address_to_name_translation[client_address] = client_name
    print(f"{client_name} has connected to the server")
    print(f"Active number of clients is: {len(clients_addresses)}")
    return client_name

def client_disconnect(client_socket: socket.socket, client_address: tuple):
    client_name = address_to_name_translation.get(client_address)
    client_socket.close()
    clients_addresses.remove(client_address)
    del address_to_name_translation[client_address]
    print(f"{client_name} has closed their connection and left the chat")
    print(f"Active number of clients is: {len(clients_addresses)}")

def socket_is_closed(client_socket: socket.socket):
    if client_socket.fileno() == -1:
        return True

def broadcast_client_disconnect(disconnected_client: socket.socket, name: str):
    disconnect_message = f"{name} has disconnected from the server".encode(FORMAT)
    for client_socket in client_sockets:
        if not socket_is_closed(client_socket):
            if disconnected_client != client_socket:
                client_socket.sendall(disconnect_message)

def server_broadcast_message(message: bytes, sender: socket.socket):
    for client_socket in client_sockets:
        if not socket_is_closed(client_socket):
            if client_socket != sender:
                client_socket.sendall(message)

def broadcast_new_client_connection(client: socket.socket, name: str):
    for client_socket in client_sockets:
        if not socket_is_closed(client_socket):
            if client_socket != client:
                connection_message = f"{name} has joined the server"
                client_socket.sendall(connection_message.encode(FORMAT))

def handle_client(client_socket: socket.socket, client_address: tuple, server: socket.socket):
    client_name = client_introduction(client_socket, client_address)
    sender = client_socket
    broadcast_new_client_connection(client_socket, client_name)
    while True:
        client_message = client_socket.recv(1024).decode(FORMAT)
        if client_message.lower() == "close":
            client_disconnect(client_socket, client_address)
            broadcast_client_disconnect(client_socket, client_name)
            break
        broadcast_message = f"{client_name}: {client_message}"
        server_broadcast_message(broadcast_message.encode(FORMAT), sender)

def main(address: tuple, server: socket.socket):
    server.bind(address)
    server.listen()
    print(f"[SERVER] is listening ...")
    while True:
        client_socket, client_address = server.accept()
        clients_addresses.append(client_address)
        client_sockets.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, server))
        thread.start()

if __name__ == "__main__":
    main(ADDRESS, SERVER)
