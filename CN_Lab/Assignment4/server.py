import socket
import threading
import time

def handle_client(client_socket, username):
    # Print a message when a user connects
    print(f'{username} connected')

    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            # Get the current time
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            # Prepare the message with sender's name and timestamp
            formatted_message = f'({current_time})\t{username}: {message}'

            print(formatted_message)

            # Broadcast message to all connected clients
            broadcast(formatted_message)

            if message.lower() == 'exit':
                break
    except:
        pass

    print(f'{username} disconnected')

    # Broadcast user left message
    user_left_message = f'{current_time} {username} left the chat'
    broadcast(user_left_message)

    client_socket.close()
    clients.remove(client_socket)

    # Check if all clients are disconnected
    if not any(is_socket_connected(client) for client in clients):
        print("No clients left. Server terminated.")
        server_socket.close()
        exit()

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            pass

def is_socket_connected(sock):
    try:
        # This will perform a non-blocking operation
        sock.getpeername()
        return True
    except socket.error:
        return False

if __name__ == "__main__":
    # Set the IP address and port
    ip_address = '127.0.0.1'
    port_number = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_address, port_number))
    server_socket.listen(5)

    print(f'Server listening on {ip_address}:{port_number}')

    clients = []

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        username = client_socket.recv(1024).decode()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
        client_handler.start()

        # Check if all clients are disconnected
        if not any(is_socket_connected(client) for client in clients):
            break
