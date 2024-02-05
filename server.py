import socket
import threading

PORT = 5050
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)
FORMAT = "utf-8"

clients = []

def handle_client(client_socket: socket.socket, client_address: tuple):
    is_connected = True
    while is_connected:
        byte_message = client_socket.recv(1024)
        msg = byte_message.decode(FORMAT)
        if msg.lower() == "close":
            print(f"client: {client_address} has closed their connection and left the chat")
            client_socket.close()
            clients.remove(client_address)
            print(f"Active number of clients is: {len(clients)}")
            break
        print(f"client: {client_address} has sent the message: {msg}")

def start_server(address: tuple):
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind(address)
    server.listen()
    print(f"[SERVER] is listening ...")
    while True:
        client_socket, client_address = server.accept()
        print(f"client: {client_address} has joined")
        clients.append(client_address)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        print(f"Active number of clients is: {len(clients)}")
        print(clients)

if __name__ == "__main__":
    start_server(ADDRESS)
