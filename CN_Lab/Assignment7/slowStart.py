cwnd = 1
add = 1
current_packet = 0
total_packets = int(input("Enter total packets to be sent: "))
ssthresh = float('inf')
timeout_packets = list(map(int, input("Enter packet numbers whose timeout occurs: ").split(' ')))
cwndn = 0
while current_packet < total_packets:
    timeout_packet = 0

    for packet in range(current_packet + 1, min(current_packet + cwnd + 1, total_packets + 1)):
        print(packet, end=' ')
        if timeout_packet == 0 and packet in timeout_packets:
            timeout_packet = packet

    current_packet = packet
    print()

    if timeout_packet != 0:
        cwndn = cwnd
        timeout_packets.remove(timeout_packet)
        cwnd = 1
        ssthresh = max(cwndn // 2, 1)  # Update ssthresh to half of cwnd
        current_packet = timeout_packet - 1  # Retransmit the packet for which timeout occurred
        timeout_packet = 0
        print(f"Timeout occurred! New ssthresh: {ssthresh}, cwnd: {cwndn}")
    elif cwnd < ssthresh:
        cwnd = min(cwnd * 2, ssthresh)
    else:
        cwnd += add
        ssthresh += add

print("Transmission completed.")
