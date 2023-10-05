try:
    file_name = input("Enter the file name: ")

    with open(file_name, 'r') as file:
        # Read and display line by line
        for line in file:
            print(line.strip())   #removes whitespaces

except FileNotFoundError:
    print(f"Error: The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
