#SUBNET INFO GENERATOR
#Author: Omkar Oak
'''
INPUTS: 
- IP Class
- IPv4 address
- Subnet Mask
OUTPUTS:
- number of hosts
- number of subnets
- network address
- broadcast address
- range of IP addresses
'''
################## AUXILLARY FUNCTIONS ######################
def checkError(cidr_notation, ip_class):
    if(ip_class!="A" and ip_class!="B" and ip_class!="C"):
        print("Invalid IP_Class")
        return
    if(int(cidr_notation.split('/')[1]) < 0 or int(cidr_notation.split('/')[1]) > 32 ):
        print("Invalid Subnet Mask")
        return
    
def calculate_subnet_info(ip_address, cidr_notation, ip_class):
    
    # Parse the CIDR notation to get the subnet bits
    subnet_bits = int(cidr_notation.split('/')[1])
    
    # Calculate the number of subnets
    if ip_class == 'A':
        num_subnets = 2 ** (subnet_bits - 8)  # Class A has a default subnet mask of /8
    elif ip_class == 'B':
        num_subnets = 2 ** (subnet_bits - 16)  # Class B has a default subnet mask of /16
    elif ip_class == 'C':
        num_subnets = 2 ** (subnet_bits - 24)  # Class C has a default subnet mask of /24
    else:
        print("Invalid IP class. Please select A, B, or C.")
        return
    
    # Calculate the number of hosts per subnet (accounting for network and broadcast addresses)
    num_hosts_per_subnet = 2 ** (32- subnet_bits) - 2

    # Calculate network and broadcast addresses, as well as the range of valid host addresses for each subnet
    network_addresses = []
    broadcast_addresses = []
    host_ranges = []
    for i in range(num_subnets):
        network = f"{ip_address.split('.')[0]}.{ip_address.split('.')[1]}.{ip_address.split('.')[2]}.{i * (256 // num_subnets)}"
        broadcast = f"{ip_address.split('.')[0]}.{ip_address.split('.')[1]}.{ip_address.split('.')[2]}.{(i + 1) * (256 // num_subnets) - 1}"
        first_host = f"{ip_address.split('.')[0]}.{ip_address.split('.')[1]}.{ip_address.split('.')[2]}.{i * (256 // num_subnets) + 1}"
        last_host = f"{ip_address.split('.')[0]}.{ip_address.split('.')[1]}.{ip_address.split('.')[2]}.{(i + 1) * (256 // num_subnets) - 2}"
        
        network_addresses.append(network)
        broadcast_addresses.append(broadcast)
        host_ranges.append(f"{first_host} - {last_host}")
    
    print(f"Number of subnets: {num_subnets}")
    print(f"Number of hosts per subnet: {num_hosts_per_subnet}")
    print("Network Addresses:")
    for network in network_addresses:
        print(network)
    print("Broadcast Addresses:")
    for broadcast in broadcast_addresses:
        print(broadcast)
    print("Range of valid host addresses:")
    for host_range in host_ranges:
        print(host_range)

def get_subnet_mask(ip_class):
    if ip_class == 'A':
        return '255.0.0.0'
    elif ip_class == 'B':
        return '255.255.0.0'
    elif ip_class == 'C':
        return '255.255.255.0'
    else:
        return None

################### MAIN METHOD ##############################
# Example usage:
#ip_address = "192.168.1.1"
#cidr_notation = "/26"
#ip_class = "C"
ip_class = input("Enter the class of IP (A,B,C): ")
ip_address = input("Enter the IP Address in IPv4 format: ")
subnet_mask = get_subnet_mask(ip_class)
if subnet_mask is None:
        print("Invalid IP class. Please select A, B, or C.")
print(f"Subnet Mask for Class {ip_class}: {subnet_mask}")


cidr_notation = input("Enter the Subnet mask in CIDR format (eg. /25): ")
checkError(cidr_notation, ip_class)
calculate_subnet_info(ip_address, cidr_notation, ip_class)


