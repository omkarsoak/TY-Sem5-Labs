import socket
import struct

# Constants
IP = '127.0.0.1'
PORT = 1234

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind((IP, PORT))

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

def CheckChecksum(message):
    rec = struct.unpack('!H', message[-2:])[0]
    actual = Checksum(message[:-2].decode('ascii'))
    return rec == actual

def main():
    answer = b""  # Use binary data to accumulate the received message

    while True:
        message, sender_address = receiver.recvfrom(1024)

        if message == b"quit":
            print("Receiver received 'quit'. Exiting.")
            break

        # Check for "done" in the received message
        if message == b"done":
            print("Complete Message: {}".format(answer.decode('ascii')))

            # Send an acknowledgment for "done"
            receiver.sendto(b"ACK", sender_address)
            break

        check = CheckChecksum(message)
        message = message[:-2]

        if check:
            answer += message
            print(f"Received message: \"{message}\". Sending ACK.")
            receiver.sendto(b"ACK", sender_address)
        else:
            print("Received corrupted message. Sending NAK.")
            receiver.sendto(b"NAK", sender_address)
    receiver.close()

if __name__ == "__main__":
    while True:
        main()
