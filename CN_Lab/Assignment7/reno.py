
def main():
    #set intial congestion window
    cwnd = 1

    #set additive increase delta
    add = 1

    #set initial packet number
    current_packet = 0

    print("Enter total packets to be sent : ", end='')
    total_packets = int(input())

    print("Enter inital slow start threshold (ssthresh) : ", end='')
    ssthresh = int(input())

    print("Enter packet numbers whose timeout occurs: ")
    timeout_packets = list(map(int, input().split(' ')))

    print("Enter packets whose 3 duplicate acks are recieved: ")
    dup_packets = list(map(int, input().split(' ')))

    while current_packet < total_packets:

        timeout_packet = 0
        dup_packet = 0

        for packet in range(current_packet + 1, min(current_packet + cwnd + 1, total_packets + 1)):
            print(packet, end=' ')
            if timeout_packet == 0 and packet in timeout_packets:
                timeout_packet = packet
            elif dup_packet == 0 and packet in dup_packets:
                dup_packet = packet

        current_packet = packet
        print()

        if timeout_packet != 0:
            timeout_packets.remove(timeout_packet)
            cwnd = 1
            ssthresh = max(ssthresh // 2, 1)
            current_packet = timeout_packet - 1
            timeout_packet = 0

        elif dup_packet != 0:
            dup_packets.remove(dup_packet)
            ssthresh = max(ssthresh // 2, 1)
            cwnd = ssthresh + 3
            current_packet = dup_packet
            dup_packet = 0

        elif cwnd < ssthresh:
            cwnd = min(cwnd * 2, ssthresh)

        else:
            cwnd += add
            ssthresh += add


if __name__ == '__main__':
    main()
