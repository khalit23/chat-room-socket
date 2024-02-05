import socket

HOSTNAME = socket.gethostname()
PORT = 5050
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)
CLIENT_SERVER = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
CLIENT_SERVER.connect(ADDRESS)
FORMAT = "utf-8"

def client_introduce():
    client_name = input("Please enter your name: ")
    CLIENT_SERVER.send(client_name.encode(FORMAT))

def send_messages():
    while True:
        client_message = input("Enter a message you'd like to send: ")
        CLIENT_SERVER.send(client_message.encode(FORMAT))
        if client_message.lower() == 'close':
            CLIENT_SERVER.close()
            break

if __name__ == "__main__":
    client_introduce()
    send_messages()
