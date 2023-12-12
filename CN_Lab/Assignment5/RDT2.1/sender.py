import socket
import hashlib

def calculate_checksum(data):
    checksum = hashlib.md5(data.encode()).hexdigest()
    return checksum

def main():
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)
    sender_address = ('localhost', 12346)

    seq_num = 0

    while True:
        message = input("Enter message to send (or 'quit' to exit): ")

        if message == 'quit':
            break

        # Add sequence number and checksum to the message
        packet = f"{seq_num}|{message}|{calculate_checksum(message)}"
        sender_socket.sendto(packet.encode(), receiver_address)

        while True:
            sender_socket.settimeout(2)  # 2-second timeout for ACK
            try:
                ack, _ = sender_socket.recvfrom(1024)
                ack_message, ack_checksum = ack.decode().split("|")
                if ack_message == f"ACK{seq_num}" and ack_checksum == calculate_checksum(ack_message):
                    print(f"ACK{seq_num} received.")
                    seq_num = 1 - seq_num  # Toggle sequence number
                    break
            except (socket.timeout, ValueError):
                print("Timeout or ACK mismatch! Resending message...")
                sender_socket.sendto(packet.encode(), receiver_address)

    sender_socket.close()

if __name__ == '__main__':
    main()
