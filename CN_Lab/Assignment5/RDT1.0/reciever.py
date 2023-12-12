import socket

def receiver():
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)
    receiver_socket.bind(receiver_address)

    message = ""

    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        if not data:
            break
        character = data.decode()
        if character == "quit":
            break
        message += character
        print("Received character:", character)

    print("Received message:", message)
    receiver_socket.close()

if __name__ == "__main__":
    receiver()
