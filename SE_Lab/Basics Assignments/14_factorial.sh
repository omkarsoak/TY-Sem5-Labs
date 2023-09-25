#!/bin/bash

calculate_factorial() {
    local num=$1
    local result=1

    for ((i = 2; i <= num; i++)); 
    do
        result=$((result * i))
    done

    echo "Factorial of $num is: $result"
}

read -p "Enter the number: " number

# Check if the input is a valid non-negative integer
if ! [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "Error: Please provide a valid non-negative integer."
    exit 1
fi

# Check if the input number is greater than 24
if [ "$number" -gt 24 ]; then
    echo "Error: Input number is greater than 24. Factorial cannot be calculated."
    exit 1
fi

calculate_factorial "$number"

