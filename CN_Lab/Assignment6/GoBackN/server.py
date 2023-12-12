import socket

# Create a UDP socket
server = socket.socket()
server.bind(('localhost', 12345))
server.listen(5)

conn, addr = server.accept()

print("Server is ready. Client has joined.")

count = 0
t = 0
# Receive data
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Received: ", data)

    # Send acknowledgement for each character of the frame as soon as it is received
    for i in data:
        conn.send(i.encode())
        print(f'Sent Acknowledgement for: {i}')
        count += 1

        if count == 2 and t < 2:
            print("Acknowledgement not sent for the next character")
            t += 1

conn.close()

print("Client has finished sending data.")
