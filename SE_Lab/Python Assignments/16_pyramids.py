def print_numeric_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        for k in range(1, i + 1):
            print(k, end=" ")
        for l in range(i - 1, 0, -1):
            print(l, end=" ")
        print()

def print_asterisk_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        
        # Print asterisks
        for k in range(1, 2 * i):
            print("*", end=" ")
        
        # Move to the next line
        print()

num = int(input("Enter the number of rows: "))
if num < 0:
    print("Negative numbers are not allowed.")
    exit

print_numeric_pyramid(num)
print_asterisk_pyramid(num)
