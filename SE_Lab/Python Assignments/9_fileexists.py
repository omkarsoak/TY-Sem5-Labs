try:
    file_name = input("Enter the file name: ")

    # Check if the file exists
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
        exists = True
    except FileNotFoundError:
        exists = False

    # Open the file for writing
    with open(file_name, 'w') as file:
        if exists:
            # File exists, so write "hello world" at the end
            file.write(file_contents.strip() + "\nhello world")

        else:
            # File didn't exist, so create it and write "hello world"
            file.write("hello world")

    print("File operation completed.")

except Exception as e:
    print(f"An error occurred: {e}")
