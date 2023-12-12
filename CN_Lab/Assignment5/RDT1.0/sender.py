import socket

def sender():
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)

    while True:
        message = input("Enter a message: ")
        sender_socket.sendto(message.encode(), receiver_address)

        if message.lower() == "quit":
            break

    sender_socket.close()

if __name__ == "__main__":
    sender()
