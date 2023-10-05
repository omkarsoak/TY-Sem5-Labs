try:
    operand1 = float(input("Enter operand-1: "))

    operator = input("Enter operator (+, -, *, /): ")

    operand2 = float(input("Enter operand-2: "))

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = operand1 / operand2
    else:
        raise ValueError("Invalid operator. Use +, -, *, or /.")

    print(f"Result: {result}")

except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")