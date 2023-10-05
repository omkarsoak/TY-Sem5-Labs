try:
    n = int(input("Enter a positive integer: "))

    if n < 0:
        raise ValueError("Factorial is defined only for positive integers.")
    
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print(f"The factorial of {n} is: {factorial}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
