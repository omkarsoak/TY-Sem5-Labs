#!/bin/bash
perform_calculation() {
    local operand1=$1
    local operator=$2
    local operand2=$3

    case $operator in
        "+")
            result=$((operand1 + operand2))
            ;;
        "-")
            result=$((operand1 - operand2))
            ;;
        "*")
            result=$((operand1 * operand2))
            ;;
        "/")
            if (( operand2 == 0 )); then
                echo "Error: Division by zero is not allowed."
                exit 1
            fi
            result=$(($operand1 / $operand2))
            ;;
        *)
            echo "Error: Invalid operator. Please use +, -, *, or /."
            exit 1
            ;;
    esac

    echo "Result: $result"
}


read -p "Enter operand 1: " operand1
read -p "Enter operand 2 (+, -, *, /): " operator
read -p "Enter operand 3: " operand3

# Check if operand 1 and operand 3 are valid numbers
if ! [[ "$operand1" =~ ^[0-9]+$ ]] || ! [[ "$operand3" =~ ^[0-9]+$ ]]; then
    echo "Error: Operand 1 and operand 3 must be valid numbers."
    exit 1
fi

# Perform the calculation
perform_calculation "$operand1" "$operator" "$operand3"

