try:
    # Input an integer
    number = int(input("Enter an integer: "))

    # Check for negative input
    if number < 0:
        raise ValueError()

    if number <= 1:
        print("Not Prime")
    elif number <= 3:
        print("Prime")
    else:
        is_prime = True
        i = 2  # Start checking from 2
        while i * i <= number:
            if number % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print("Prime")
        else:
            print("Not Prime")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
