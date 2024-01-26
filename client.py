import socket

HOSTNAME = socket.gethostname()
PORT = 5050
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)
CLIENT_SERVER = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
