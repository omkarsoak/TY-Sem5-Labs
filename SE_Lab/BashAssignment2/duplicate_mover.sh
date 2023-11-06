#!/bin/bash

read -p "Enter the source folder path: " source_folder
read -p "Enter the target folder path: " target_folder

# Ensure target folder exists
mkdir -p "$target_folder"

# Find and move duplicate files
find "$source_folder" -type f -exec md5sum {} + | 
    sort | 
    uniq -w32 -dD | 
    cut -d' ' -f3- | 
    xargs -I {} mv {} "$target_folder"

echo "Duplicate files moved to $target_folder"


#find "$source_folder" -type f -exec md5sum {} +: Finds all files in the source folder and calculates the MD5 checksum for each file.
#sort: Sorts the checksums.
#uniq -w32 -dD: Identifies and keeps only the duplicate checksums.
#cut -d' ' -f3-: Extracts the file paths from the duplicate checksums.
#xargs -I {} mv {} "$target_folder": Moves the duplicate files to the target folder.

