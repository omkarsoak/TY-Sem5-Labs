cwnd = 1
add = 1
current_packet = 0
total_packets = int(input("Enter total packets to be sent: "))
ssthresh = float('inf')
timeout_packets = list(map(int, input("Enter packet numbers whose timeout occurs: ").split(' ')))

cwndn = 0
duplicate_acks = 0  # Track the number of duplicate ACKs received

# Set the threshold for triple duplicate ACKs 
triple_duplicate_ack_threshold = 4

while current_packet < total_packets:
    timeout_packet = 0

    for packet in range(current_packet + 1, min(current_packet + cwnd + 1, total_packets + 1)):
        print(packet, end=' ')
        if timeout_packet == 0 and packet in timeout_packets:
            timeout_packet = packet

    current_packet = packet
    print()

    if timeout_packet != 0:
        # Handle timeout event
        cwndn = cwnd
        timeout_packets.remove(timeout_packet)
        cwnd = 1
        ssthresh = max(cwndn // 2, 1)  # Update ssthresh to half of cwnd
        current_packet = timeout_packet - 1  # Retransmit the packet for which timeout occurred
        timeout_packet = 0
        duplicate_acks = 0  # Reset duplicate ACK count
        print(f"Timeout occurred for packet {current_packet + 1}! New ssthresh: {ssthresh}, cwnd: {cwndn}")
    else:
        duplicate_acks += 1  

        if duplicate_acks >= triple_duplicate_ack_threshold:
            # Handle triple duplicate ACK event as if it were a timeout
            cwndn = cwnd
            cwnd = 1
            ssthresh = max(cwndn // 2, 1)
            current_packet -= triple_duplicate_ack_threshold  # Retransmit the packet for which triple duplicate ACKs occurred
            duplicate_acks = 0  # Reset duplicate ACK count
            print(f"Triple Duplicate ACKs occurred for packet {current_packet + 1}! New ssthresh: {ssthresh}, cwnd: {cwndn}")
        elif cwnd < ssthresh:
            cwnd = min(cwnd * 2, ssthresh)
        else:
            cwnd += add

print("Transmission completed.")
