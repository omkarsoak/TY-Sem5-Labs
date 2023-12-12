import socket
import struct
import random

# Constants
IP = '127.0.0.1'
PORT = 1234

def Checksum(packet):
    checksum = 0
    for i in range(0, len(packet), 2):
        data = packet[i:i + 2]
        if len(data) == 2:
            value = (ord(data[0]) << 8) + ord(data[1])
            checksum += value
        else:
            value = ord(data)
            checksum += value

    while (checksum >> 16) > 0:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)

    return (~checksum) & 0xFFFF

def GenerateError(checksum):
    prob = 0.2
    rand = random.random()
    if rand < prob:
        return checksum - 1
    else:
        return checksum

def main():
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter your message (or 'quit' to quit): ")
        if message.lower() == 'quit':
            sender.sendto(message.encode('ascii'), (IP, PORT))
            break

        packets = [message[i:i + 4] for i in range(0, len(message), 4)]
        i = 0

        while i < len(packets):
            checksumValue = Checksum(packets[i])
            newBits = GenerateError(checksumValue)
            new_message = packets[i].encode('ascii') + struct.pack('!H', newBits)
            sender.sendto(new_message, (IP, PORT))
            print("Sending: {}".format(packets[i]))

            # Receive acknowledgment
            sender.settimeout(5)  # Adjust the timeout as needed
            try:
                acknowledgement, _ = sender.recvfrom(1024)
                if acknowledgement.decode('ascii') == "ACK":
                    print("Acknowledgment received")
                    i += 1
                else:
                    print("Negative acknowledgment received")
                    print("Retransmitting packet")
            except socket.timeout:
                print("Acknowledgment not received. Retransmitting packet")

        if i < len(packets):
            print("Transmission failed.")
        else:
            print("Transmission complete.")

    sender.close()

if __name__ == "__main__":
    main()
