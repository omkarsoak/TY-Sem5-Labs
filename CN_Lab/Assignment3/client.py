import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP and port to connect to
server_ip = "127.0.0.1"  # Change this to the server's IP
server_port = 12345     # Use the same port as the server

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to the server")

while True:
    # Ask the user for input
    user_message = input("Client: ")
    
    # Send the user's input to the server
    client_socket.send(user_message.encode("utf-8"))

    # Check for exit condition
    if user_message.lower() == 'exit':
        break

    # Receive and print the server's response
    server_response = client_socket.recv(1024).decode("utf-8")
    print(f"Server: {server_response}")

# Close the socket
client_socket.close()
