import socket

def main():
    # Create a TCP/IP socket
    server = socket.socket()
    server.bind(('localhost', 12345))
    server.listen(5)

    print("Server is ready. Waiting for a client to join...")

    # Accept the connection
    conn, addr = server.accept()

    print("Client has joined. Ready to receive data.")

    while True:
        try:
            data = conn.recv(1024).decode()
        except socket.timeout:
            continue

        if data.lower() == 'exit':
            break

        print('Received: ', data)
        handle_ack(conn, data)

    conn.close()

def handle_ack(conn, data):
    conn.settimeout(3)
    try:
        ack = conn.recv(1024).decode()
        print('Received: ', ack)
    except socket.timeout:
        print('Timeout. Resending the packet')
        conn.send(data.encode())
        print('Sent:', data)

if __name__ == '__main__':
    main()
