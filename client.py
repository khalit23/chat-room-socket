import socket
import threading

HOSTNAME = socket.gethostname()
PORT = 5050
IP = socket.gethostbyname(HOSTNAME)
ADDRESS = (IP, PORT)
FORMAT = "utf-8"
CLIENT_SERVER = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

def client_introduce(client_server: socket.socket):
    client_name = input("Please enter your name: ")
    client_server.send(client_name.encode(FORMAT))

def receive_messages(client_server: socket.socket):
    while True:
        try:
            received_message = client_server.recv(1024).decode(FORMAT)
            print(received_message)
        except ConnectionAbortedError as error:
            print(f"Connection error: {error}")

def send_message(client_server: socket.socket):
    while True:
        client_message = input("")
        client_server.send(client_message.encode(FORMAT))
        if client_message.lower() == 'close':
            client_server.close()
            break

def main(client_server: socket.socket, address: tuple):
    client_server.connect(address)
    client_introduce(client_server)

    receive_message_thread = threading.Thread(target=receive_messages, args=(CLIENT_SERVER,))
    receive_message_thread.start()
    
    send_message_thread = threading.Thread(target=send_message, args=(CLIENT_SERVER,))
    send_message_thread.start()

if __name__ == "__main__":
    main(CLIENT_SERVER, ADDRESS)
