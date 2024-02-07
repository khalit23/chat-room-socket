import socket
import threading

HOSTNAME = socket.gethostname()
PORT = 5050
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)
FORMAT = "utf-8"

def client_introduce(client_server: socket.socket):
    client_name = input("Please enter your name: ")
    client_server.send(client_name.encode(FORMAT))

def send_messages(client_server: socket.socket):
    while True:
        client_message = input("Enter a message you'd like to send: ")
        client_server.send(client_message.encode(FORMAT))
        if client_message.lower() == 'close':
            client_server.close()
            break

def receive_messages(client_server: socket.socket):
    while True:
        try:
            received_message = client_server.recv(1024).decode(FORMAT)
            print(received_message)
        except client_server.timeout:
            break

if __name__ == "__main__":
    CLIENT_SERVER = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    CLIENT_SERVER.connect(ADDRESS)
    client_introduce(CLIENT_SERVER)
    message_thread = threading.Thread(target=send_messages, args=CLIENT_SERVER)
    receive_message_thread = threading.Thread(target=receive_messages, args=CLIENT_SERVER)
    receive_message_thread.start()
    message_thread.start()