#!/bin/bash

# Function to find the largest of three numbers
find_largest() {
    local num1=$1
    local num2=$2
    local num3=$3
    local largest=$num1

    if ((num2 > largest)); then
        largest=$num2
    fi

    if ((num3 > largest)); then
        largest=$num3
    fi

    echo "Largest number: $largest"
}

# the command line arguments
read -p "Enter the 1st number: " num1
read -p "Enter the 2nd number: " num2
read -p "Enter the 3rd number: " num3

find_largest "$num1" "$num2" "$num3"

