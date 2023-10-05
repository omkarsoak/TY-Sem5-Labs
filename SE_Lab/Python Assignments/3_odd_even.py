try:
    num = int(input("Enter the number: "))
    if num < 0:
        raise ValueError()
    if(num%2==0): 
        print("It is even")
    else: 
        print("It is odd")
except ValueError:
    print("Invalid input. Please enter a valid integer.")