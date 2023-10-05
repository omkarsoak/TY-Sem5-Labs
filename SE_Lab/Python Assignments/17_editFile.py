filename = input("Enter the file name: ")

content = """Cat
dog
bear
hello
elephant
hello
tiger
hello
horse"""

# Write the content to a file
with open(filename, "w") as file:
    file.write(content)

# Display the modified file
with open(filename, "r") as file:
    modified_content = file.read()
    print(modified_content)

# Read the file, filter out lines containing "hello," and write back to the file
filtered_lines = []
with open(filename, "r") as file:
    for line in file:
        if "hello" not in line:
            filtered_lines.append(line)

with open(filename, "w") as file:
    file.writelines(filtered_lines)

# Display the modified file
with open(filename, "r") as file:
    modified_content = file.read()
    print(modified_content)
