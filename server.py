import socket
import threading

PORT = 5050
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)

def start_server(address: tuple):
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind(address)
    server.listen()
    while True:
        print(f"[SERVER] is starting ...")
        client_socket, client_address = server.accept()

if __name__ == "__main__":
    start_server(ADDRESS)
