#!/bin/bash

print_upside_star_pyramid() {
    local height=$1
    for ((i = height; i >= 1; i--)); do
        for ((j = 1; j <= height - i; j++)); do
            echo -n " "
        done
        for ((j = 1; j <= 2 * i - 1; j++)); do
            echo -n "*"
        done
        echo
    done
}

print_upside_number_pyramid() {
    local height=$1
    for ((i = height; i >= 1; i--)); do
        for ((j = 1; j <= height - i; j++)); do
            echo -n " "
        done
        for ((j = 1; j <= 2 * i - 1; j++)); do
            echo -n "$j"
        done
        echo
    done
}

print_downside_star_pyramid() {
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

print_downside_number_pyramid() {
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

while true; do
    echo "Choose the type of pyramid:"
    echo "1. Upside Star Pyramid"
    echo "2. Upside Number Pyramid"
    echo "3. Downside Star Pyramid"
    echo "4. Downside Number Pyramid"
    echo "5. Exit"
    
    read -p "Enter your choice (1/2/3/4/5): " choice

    case $choice in
        1)
            read -p "Enter the height: " height
            print_upside_star_pyramid "$height"
            ;;
        2)
            read -p "Enter the height: " height
            print_upside_number_pyramid "$height"
            ;;
        3)
            read -p "Enter the height: " height
            print_downside_star_pyramid "$height"
            ;;
        4)
            read -p "Enter the height: " height
            print_downside_number_pyramid "$height"
            ;;
        5)
            echo "Exiting."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please select a valid option."
            ;;
    esac
done

