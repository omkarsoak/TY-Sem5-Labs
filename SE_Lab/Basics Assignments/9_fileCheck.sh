#!/bin/bash

# Extract the filename from the command line argument
filename="$1"

# Check if the file exists
if [ -e "$filename" ]; then
    # File exists, append "hello world" to it
    echo "hello world" >> "$filename"
    echo "Text appended to existing file: $filename"
else
    # File does not exist, create it and write "hello world"
    touch "$filename"
    echo "hello world" > "$filename"
    echo "File created with 'hello world': $filename"
fi

