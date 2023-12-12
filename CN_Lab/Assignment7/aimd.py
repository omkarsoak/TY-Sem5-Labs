no_of_packets = int(input("Number of transmissions: "))
ssthresh = float('inf')
timeout_string = input("Points where timeout occurs: ")
timeout = sorted(map(int, timeout_string.split()))
timeout.append(float('inf'))
cwnd = 1
i = 1  #current packet being transmitted
itr = 1 #for RTT

print("RTT\t Segments")
while i <= no_of_packets:
    if i+cwnd > timeout[0]:
        print(itr, end="\t")
        for j in range(i, i+cwnd):
            if j > no_of_packets:
                break
            print(j, end=" ")
        itr += 1
        print()
        i = timeout.pop(0)
        ssthresh = cwnd // 2
        cwnd = ssthresh

    #if the current segment of transmissions does not exceed the next timeout point
    else:
        print(itr, end="\t")
        for j in range(i, i+cwnd):
            if j > no_of_packets:
                break
            print(j, end=" ")
        print()
        itr += 1
        i += cwnd
        cwnd += 1



