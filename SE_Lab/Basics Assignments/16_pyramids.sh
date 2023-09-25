#!/bin/bash
print_number_pyramid() {
    local height=$1
    for ((i = 1; i <= height; i++)); do
        for ((j = 1; j <= height - i; j++)); do
            echo -n " "
        done
        for ((j = 1; j <= 2 * i - 1; j++)); do
            echo -n "$j"
        done
        echo
    done
}

print_star_pyramid() {
    local height=$1
    for ((i = 1; i <= height; i++)); do
        for ((j = 1; j <= height - i; j++)); do
            echo -n " "
        done
        for ((j = 1; j <= 2 * i - 1; j++)); do
            echo -n "*"
        done
        echo
    done
}


read -p "Enter the height: " height
# Check if the input is a valid non-negative integer
if ! [[ "$height" =~ ^[0-9]+$ ]]; then
    echo "Error: Please provide a valid non-negative integer as the pyramid height."
    exit 1
fi

# Menu to choose pyramid type
echo "Choose the type of pyramid:"
echo "1. Number Pyramid"
echo "2. Star Pyramid"
echo "3. Both"

read -p "Enter your choice (1/2/3): " choice

case $choice in
    1)
        print_number_pyramid "$height"
        ;;
    2)
        print_star_pyramid "$height"
        ;;
    3)
        print_number_pyramid "$height"
        print_star_pyramid "$height"
        ;;
    *)
        echo "Invalid choice. Exiting."
        ;;
esac

