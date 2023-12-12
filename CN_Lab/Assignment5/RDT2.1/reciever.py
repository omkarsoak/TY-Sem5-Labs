import socket
import hashlib

def calculate_checksum(data):
    checksum = hashlib.md5(data.encode()).hexdigest()
    return checksum

def main():
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)
    receiver_socket.bind(receiver_address)

    expected_seq_num = 0

    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        packet = data.decode()
        seq_num, message, received_checksum = packet.split("|")

        if int(seq_num) == expected_seq_num and received_checksum == calculate_checksum(message):
            print(f"Received message: {message}")
            receiver_socket.sendto(f"ACK{seq_num}|{calculate_checksum(f'ACK{seq_num}')}".encode(), sender_address)
            expected_seq_num = 1 - expected_seq_num  # Toggle expected sequence number
        else:
            # Send NAK for incorrect packets
            receiver_socket.sendto(f"NAK{expected_seq_num}|{calculate_checksum(message)}".encode(), sender_address)

    receiver_socket.close()

if __name__ == '__main__':
    main()
