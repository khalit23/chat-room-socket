import socket
import threading

PORT = 5050
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)

def start_server(address: tuple):
    pass

if __name__ == "__main__":
    start_server(ADDRESS)
