#!/bin/bash

# Extract the integer from the command line argument
read -p "Enter the number: " number

# Check if the input is a valid integer
if ! [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "Error: Please provide a valid integer."
    exit
fi

# Function to check if a number is prime
is_prime() {
    num=$1
    if [ "$num" -le 1 ]; then
        echo "Not Prime"
        exit
    fi

    for ((i = 2; i * i <= num; i++)) 
    do
        if [ $((num % i)) -eq 0 ]; then
            echo "Not Prime"
            exit
        fi
    done

    echo "Prime"
}

# Check if the given number is prime
result=$(is_prime "$number")
echo "$number is $result."

