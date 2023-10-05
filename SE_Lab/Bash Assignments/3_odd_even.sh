#!/bin/bash

# Extract the number from the command line argument
read -p "Enter the number: " number

# Check if the input is a valid integer
if ! [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "Error: Please provide a valid integer."
    exit 1
fi

# Check if the given number is odd or even
if [ $((number % 2)) -eq 0 ]; then
    echo "$number is even."
else
    echo "$number is odd."
fi

