import socket
import struct
import random

def Checksum(packet):
    checksum = 0
    for i in range(0, len(packet), 2):
        data = packet[i:i+2]
        if len(data) == 2:
            value = (ord(data[0]) << 8) + ord(data[1])
            checksum += value
        else:
            value = ord(data)
            checksum += value
    while (checksum >> 16) > 0:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    return (~checksum) & 0xFFFF

def Check_Checksum(message):
    rec = (struct.unpack('!H', message[-2:]))[0]
    actual = Checksum(message[:-2].decode('ascii'))
    if rec == actual:
        return True
    else:
        return False

def main():
    receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver.bind(('127.0.0.1', 1234))
    receiver.listen(5)
    
    receiver_socket, addr = receiver.accept()
    answer = ""
    prev_seq = 1
    while True:
        message = receiver_socket.recv(1024)
        if message.startswith("exit".encode('ascii')):
            print("Exiting the program.")
            break

        if len(message) < 3:
            print("Erroneous packet received")
            continue

        if message.startswith("ACK".encode('ascii')):
            seq = int(message[3:4].decode('ascii'))
            ack = "ACK"
            print("Acknowledgement received for sequence: {}".format(seq))
            receiver_socket.send((ack + str(seq % 2)).encode('ascii'))
        else:
            seq = int(message[0:1].decode('ascii'))
            message = message[1:]
            check = Check_Checksum(message)

            if not check:
                print("Erroneous packet received")
                continue

            message = message[:-2].decode('ascii')

            if prev_seq % 2 != seq % 2:
                answer += message
                prev_seq = seq % 2
            ack = "ACK"
            print("Current packet received: {}".format(message))
            receiver_socket.send((ack + str(seq % 2)).encode('ascii'))

    receiver_socket.close()
    print("Received complete message: {}".format(answer))

if __name__ == "__main__":
    main()
