try:
    file1_name = input("Enter the first file name: ")
    file2_name = input("Enter the second file name: ")

    with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
        content1 = file1.read()
        content2 = file2.read()

    if content1 == content2:
        print("The contents of the files are the same.")
    else:
        print("The contents of the files are different.")

except FileNotFoundError:
    print("Error: One or both files not found.")
except Exception as e:
    print(f"An error occurred: {e}")