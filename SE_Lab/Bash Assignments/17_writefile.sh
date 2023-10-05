#!/bin/bash

filename=$1

# Write the contents to the file
echo "Cat
dog
bear
hello
elephant
hello
tiger
hello
horse" > "$filename"

# Delete lines containing the word "hello"
grep -v "hello" "$filename" > temp.txt
mv temp.txt "$filename"

echo "content appended"

