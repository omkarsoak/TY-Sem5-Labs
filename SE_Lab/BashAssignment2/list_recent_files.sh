#!/bin/bash

while true; do
    echo "Menu:"
    echo "Find the top 10 size files created in the last 20 days:"
    echo "1. on the entire system"
    echo "2. in a specific directory"
    echo "3. Exit"

    read -p "Enter your choice (1/2/3): " choice

    case $choice in
        1)
            echo "on the entire system..."
            find / -type f -ctime -20 -exec du -h {} + 2>/dev/null | sort -rh | head -n 10
            exit 0
            ;;
        2)
            read -p "Enter the directory path: " dir_path
            echo "in $dir_path..."
            find "$dir_path" -type f -ctime -20 -exec du -h {} + | sort -rh | head -n 10
            exit 0
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

#Uses the find command to locate files on the entire system (/) or give a path
#Filters files based on their creation time (-ctime -20 for files created in the last 20 days).
#Uses du -h to get the human-readable sizes of the files.
#Sorts the files by size in reverse order (sort -rh).
#Displays the top 10 files using head -n 10.
