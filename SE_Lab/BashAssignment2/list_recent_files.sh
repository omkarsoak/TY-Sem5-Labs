#!/bin/bash

while true; do
    echo "Menu:"
    echo "1. Find the top 10 size files created in the last 20 days on the entire system"
    echo "2. Find the top 10 size files created in the last 20 days in a specific directory"
    echo "3. Exit"

    read -p "Enter your choice (1/2/3): " choice

    case $choice in
        1)
            echo "Finding the top 10 size files created in the last 20 days on the entire system..."
            find / -type f -ctime -20 -exec du -h {} + 2>/dev/null | sort -rh | head -n 10
            ;;
        2)
            read -p "Enter the directory path: " dir_path
            echo "Finding the top 10 size files created in the last 20 days in $dir_path..."
            find "$dir_path" -type f -ctime -20 -exec du -h {} + | sort -rh | head -n 10
            ;;
        3)
            echo "Script exited!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter 1, 2, or 3."
            ;;
    esac
done

