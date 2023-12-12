import time
import socket

# Create a UDP socket
client_socket = socket.socket()
client_socket.connect(('localhost', 12345))

print("Client is ready.")
while True:
    # Input frame and window size
    frame = input("Enter the frame to be sent (enter 'exit' to quit) : ")
    if (frame.lower() == 'exit'):
        break
    window = int(input("Enter the window size: "))

    count_ack = 0

    # Send the data - window by window
    for i in range(0, len(frame), window):
        # Send each character of the window with a delay of 1 second
        for j in frame[i:i+window]:
            client_socket.send(j.encode())
            time.sleep(1)
            print(f'Sent: {j}')

        client_socket.settimeout(3)
        try:
            ack = client_socket.recv(1024).decode()
            print('Received Acknowledgment: ', ack)
            count_ack += 1
        except socket.timeout:
            if count_ack == len(frame[i:i+window]):
                print("Acknowledgment received for all the characters in the window")
                print("Sliding the window")
            else:
                print("Acknowledgment not received for all the characters in the window")
                print("Resending the frame")
                break
            count_ack = 0

client_socket.close()

print("Client has finished sending data.")
