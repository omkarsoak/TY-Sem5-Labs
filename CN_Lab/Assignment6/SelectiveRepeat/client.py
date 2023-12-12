import socket
import time

def main():
    # Create a TCP/IP socket
    client = socket.socket()
    client.connect(('localhost', 12345))

    while True:
        data = input('Enter data (type "exit" to quit): ')
        if data == 'exit':
            break

        window = int(input('Enter the window size: '))
        send_packet(client, data, window)

    client.close()

def send_packet(client, data, window):
    for i in range(0, len(data), window):
        window_data = data[i:i + window]
        ack_received = send_frame(client, window_data)
        
        if ack_received != len(window_data):
            print("Resending the frame")
            resend_frame(client, window_data)

def send_frame(client, frame):
    count_ack = 0
    for i in frame:
        client.send(i.encode())
        time.sleep(1)
        print(f'Sent: {i}')
        count_ack += handle_ack(client)
    return count_ack

def handle_ack(client):
    client.settimeout(3)
    count_ack = 0
    try:
        while True:
            ack = client.recv(1024).decode()
            print('Received:', ack)
            count_ack += 1
    except socket.timeout:
        return count_ack

def resend_frame(client, frame):
    for i in frame:
        client.send(i.encode())
        time.sleep(1)
        print(f'Resent: {i}')
    print("Resent frame:", frame)

if __name__ == '__main__':
    main()
