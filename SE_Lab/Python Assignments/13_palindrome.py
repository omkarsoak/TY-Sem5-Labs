try:
    input_string = input("Enter a string: ")

    # Remove spaces and convert to lowercase for case-insensitive comparison
    input_string = input_string.replace(" ", "").lower()

    if input_string == input_string[::-1]:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")

except Exception as e:
    print(f"An error occurred: {e}")
