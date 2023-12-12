import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

def send_message():
    while True:
        try:
            message = input()
            client_socket.send(message.encode())

            if message.lower() == 'exit':
                # If user types 'exit', break out of the loop
                break
        except:
            break

if __name__ == "__main__":
    # Create a client socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    # Prompt the user for username and send it to the server
    username = input("Enter your username: ")
    client_socket.send(username.encode())
    
    # Start a thread for receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    
    # Start a thread for sending messages
    send_thread = threading.Thread(target=send_message)
    
    # Start both threads
    receive_thread.start()
    send_thread.start()
