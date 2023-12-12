import math
from collections import defaultdict

# Input packet size and link capacity.
dataLinkCapacity = int(input("Enter data link capacity in bytes (MTU): "))
datagramSize = int(input("Enter datagram size in bytes: "))
datagramHeaderSize = int(input("Enter datagram header size in bytes: "))

datagramPayloadSize = datagramSize - datagramHeaderSize
dataLinkPayloadCapacity = dataLinkCapacity - 20

if datagramPayloadSize < dataLinkPayloadCapacity:
    print("No fragmentation required!!")
else:
    # Calculate the number of fragments required
    noOfFragments = math.ceil(datagramPayloadSize / dataLinkPayloadCapacity)
    
    # Calculate the maximum payload size that is divisible by 8
    maxPayloadDivisibleBy8 = (dataLinkPayloadCapacity // 8) * 8
    
    if maxPayloadDivisibleBy8 < dataLinkPayloadCapacity:
        print(f"Maximum payload size divisible by 8: {maxPayloadDivisibleBy8} bytes")
    else:
        maxPayloadDivisibleBy8 = dataLinkPayloadCapacity

    print("Max data in each segment: ",dataLinkCapacity-datagramHeaderSize)
    print("Number of fragments:", noOfFragments)

    # Initialize a dictionary to store fragment information
    dict = defaultdict(lambda: {'MF': 0, 'FragmentLength': 0, 'offset': 0})
    offset = 0

    for i in range(noOfFragments):
        dict[i]['MF'] = 1 if i != noOfFragments - 1 else 0
        dict[i]['FragmentLength'] = 20 + maxPayloadDivisibleBy8
        dict[i]['offset'] = offset // 8  # Divide offset by 8

        offset += maxPayloadDivisibleBy8

    #for key in dict:
    #    print("Fragment", key + 1, ":", dict[key])
    
    # Print table header
    print("{:<15} {:<18} {:<5} {:<5} {:<7}".format("Fragment", "FragmentLength", "DF", "MF" , "Offset"))
    #print("="*45)

    # Print table rows
    for key, values in dict.items():
        print("{:<15} {:<18} {:<5} {:<5} {:<7}".format(key+1, values['FragmentLength'], 0, values['MF'] , values['offset']))
