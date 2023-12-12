import socket

def main():
    # Create a TCP/IP socket
    server = socket.socket()
    server.bind(('localhost', 12345))
    server.listen(5)
    print('Server is ready. Waiting for connections...')

    # Accept the connection
    conn, addr = server.accept()
    print('Client', addr, 'has joined.')

    tt = 0
    while True:
        data = conn.recv(1024).decode()

        if data == 'exit':
            break

        print('Received:', data)

        if data == 'test' and tt == 0:
            print('Simulating acknowledgment not sent')
            data = conn.recv(1024).decode()
            print('Received:', data)
            conn.send('test'.encode())
            print('Sent: Acknowledgment')
            tt = 1

        else:
            send_acknowledgment(conn, data)

    conn.close()

def send_acknowledgment(conn, data):
    conn.send(str(data).encode())
    print('Sent Acknowledgment:', data)

if __name__ == '__main__':
    main()
