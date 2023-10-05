#!/bin/bash

# Function to check if a year is a leap year
is_leap_year() {
    local year=$1
    if (( (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0) )); then
        return 0
    else
        return 1
    fi
}

read -p "Enter the starting year: " starting_year

# Check if the starting year is a leap year
if is_leap_year "$starting_year"; then
    echo "$starting_year is a leap year."
else
    echo "$starting_year is not a leap year."
fi

leap_year_counter=0
current_year="$starting_year"

# Iterate through years and find the next 10 leap years starting from the next year
while [ "$leap_year_counter" -lt 10 ]; 
do
    ((current_year++))
    if is_leap_year "$current_year"; then
        echo "$current_year"
        ((leap_year_counter++))
    fi
done

