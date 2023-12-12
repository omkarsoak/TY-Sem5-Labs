import socket
import struct
import random
import time

# Constants
IP = '127.0.0.1'
PORT = 1234
MAX_RETRANSMISSION_ATTEMPTS = 3  # Maximum number of retransmission attempts

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

def GenerateError(checksum):
    prob = 0.2
    rand = random.random()
    if rand < prob:
        return checksum - 1
    else:
        return checksum

def main():
    sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender.connect((IP, PORT))

    while True:
        message = input("Enter your message (or 'quit' to quit): ")
        if message.lower() == 'quit':
            break

        packets = [message[i:i + 5] for i in range(0, len(message), 5)]
        i = 0

        retransmission_attempts = 0
        seq = 0  # Initialize sequence number
        while i < len(packets):
            checksumValue = Checksum(packets[i])
            newBits = GenerateError(checksumValue)
            new_message = (str(seq % 2)).encode('ascii') + (packets[i]).encode('ascii') + struct.pack('!H', newBits)
            sender.send(new_message)
            print("Sending {}".format(packets[i]))

            # Receive acknowledgment with timeout
            sender.settimeout(5)  # Adjust the timeout as needed
            try:
                acknowledgement = sender.recv(1024).decode('ascii')
                if acknowledgement[:4] == "ACK" + str(seq % 2):
                    print("Acknowledgment received")
                    i += 1
                    seq = 1 - seq  # Toggle sequence number
                else:
                    print("Erroneous message received")
                    print("Retransmitting packet")
                    retransmission_attempts += 1
                    if retransmission_attempts >= MAX_RETRANSMISSION_ATTEMPTS:
                        print("Maximum retransmission attempts reached. Exiting.")
                        break
            except socket.timeout:
                print("Acknowledgment not received. Retransmitting packet")
                retransmission_attempts += 1
                if retransmission_attempts >= MAX_RETRANSMISSION_ATTEMPTS:
                    print("Maximum retransmission attempts reached. Exiting.")
                    break

        if i < len(packets):
            print("Transmission failed.")
        else:
            print("Transmission complete.")

    sender.close()

if __name__ == "__main__":
    main()
