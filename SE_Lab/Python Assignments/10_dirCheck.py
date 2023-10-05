import os
try:
    directory_name = input("Enter the directory name: ")

    # Check if the directory exists
    if not os.path.exists(directory_name):
        # If the directory does not exist, create it
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists.")

except Exception as e:
    print(f"An error occurred: {e}")
