#!/bin/bash

# Extract the radius from the command line argument
radius="$1"

# Check if the input is a valid number
if ! [[ "$radius" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    echo "Error: Please provide a valid number as the radius."
    exit
fi

# Function to calculate the area of a circle
calculate_area() {
    local r=$1
    local pi=3.14159
    echo "Area: $(echo "$pi * $r * $r" | bc) square units"
}

# Function to calculate the circumference of a circle
calculate_circumference() {
    local r=$1
    local pi=3.14159
    echo "Circumference: $(echo "2 * $pi * $r" | bc) units"
}

# Calculate and display the area and circumference of the circle
calculate_area "$radius"
calculate_circumference "$radius"

