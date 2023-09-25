#!/bin/bash

calculate_factorial() {
    local n=$1

    if [ $n -lt 0 ]; then
        echo "Error: Factorial is not defined for negative numbers."
        return
    fi

    if [ $n -eq 0 ]; then
        echo "Factorial of 0 is 1"
        return
    fi

    result=$(echo "1" | bc)

    for ((i = 1; i <= n; i++)); do
        result=$(echo "$result * $i" | bc)
    done

    echo "Factorial of $n is $result"
}

read -p "Enter the number: " number

# Check if the input is a valid non-negative integer
if ! [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "Error: Please provide a valid non-negative integer."
    exit 1
fi

# Check if the input number is greater than 24
if [ "$number" -gt 200 ]; then
    echo "Error: Input number is greater than 200. Factorial cannot be calculated."
    exit 1
fi

calculate_factorial "$number"

