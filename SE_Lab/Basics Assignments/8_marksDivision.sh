#!/bin/bash
calculate_result() {
    local average_marks=$1

    if (( average_marks >= 80 )); then
        echo "Result: First Division (I-Division)"
    elif (( average_marks >= 60 )); then
        echo "Result: Second Division (II-Division)"
    elif (( average_marks >= 40 )); then
        echo "Result: Third Division (III-Division)"
    else
        echo "Result: Fail"
    fi
}

# Input: Number of students and subjects
read -p "Enter the number of students: " num_students
read -p "Enter the number of subjects: " num_subjects

for ((s=1; s<=$num_students; s++)); do
    total_marks=0

    echo "Student $s:"
    # Input: Marks for each subject for the current student
    for ((i=1; i<=$num_subjects; i++)); do
        read -p "Enter marks for Subject $i: " marks
        # Check if the input marks are valid integers
        if ! [[ "$marks" =~ ^[0-9]+$ ]]; then
            echo "Error: Please provide valid integer marks for all subjects."
            exit
        fi

        total_marks=$((total_marks + marks))
    done

    average_marks=$(( total_marks / num_subjects ))

    # Call function to calculate and display result for the current student
    echo "Student $s - $(calculate_result "$average_marks")"
done

