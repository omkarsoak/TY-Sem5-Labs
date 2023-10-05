#!/bin/bash

is_palindrome() {
    local input="$1"
    local reversed=""
    local len=${#input}

    # Reverse the string
    for (( i=len-1; i>=0; i--)); 
    do
        reversed="${reversed}${input:i:1}"
    done

    if [ "$input" == "$reversed" ]; then
        return 0  
    else
        return 1 
    fi
}


read -p "Enter the string: " input_string

# Check if the input string is a valid non-empty string
if [ -z "$input_string" ]; then
    echo "Error: Please provide a non-empty string."
    exit
fi

# Remove spaces and convert to lowercase for case-insensitive palindrome check
input_string="$(echo "$input_string" | tr -d ' ' | tr '[:upper:]' '[:lower:]')"


if is_palindrome "$input_string"; then
    echo "$input_string is a palindrome."
else
    echo "$input_string is not a palindrome."
fi

