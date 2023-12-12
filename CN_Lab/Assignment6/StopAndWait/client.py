import socket
import time

def main():
    # Create a TCP/IP socket
    client = socket.socket()
    client.connect(('localhost', 12345))

    while True:
        data = input('Enter data (type "exit" to quit): ')
        client.send(data.encode())

        if data == 'exit':
            break

        print('Sent:', data)
        handle_ack(client)

    client.close()

def handle_ack(client):
    client.settimeout(3)
    try:
        ack = client.recv(1024).decode()
        print('Received:', ack)
    except socket.timeout:
        print('Timeout. Resending the packet')
        resend_packet(client)

def resend_packet(client):
    data = input('Resending the packet. Enter the same data: ')
    client.send(data.encode())
    print('Sent:', data)
    handle_ack(client)

if __name__ == '__main__':
    main()
