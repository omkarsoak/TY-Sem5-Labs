import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
host = "127.0.0.1"  # You can change this to your server's IP
port = 12345       # Choose a port (e.g., 12345)
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

while True:
    # Receive data from the client
    client_message = client_socket.recv(1024).decode("utf-8")
    print(f"Client: {client_message}")

    # Check for exit condition
    if client_message.lower() == 'exit':
        break

    # Send a response back to the client
    server_response = input("Server: ")
    client_socket.send(server_response.encode("utf-8"))

# Close the sockets
client_socket.close()
server_socket.close()
