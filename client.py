import socket

HOSTNAME = socket.gethostname()
PORT = 5050
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)
CLIENT_SERVER = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
CLIENT_SERVER.connect(ADDRESS)
FORMAT = "utf-8"

while True:
    client_message = input("Enter a message you'd like to send: ")
    if client_message.lower() == "close":
        CLIENT_SERVER.close()
        break
    else:
        CLIENT_SERVER.send(client_message.encode(FORMAT))
