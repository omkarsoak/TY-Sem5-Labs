#!/bin/bash

filename=$1

if [ ! -f "$filename" ]; then
    echo "File '$filename' not found."
    exit 1
fi

while IFS= read -r line; do
    echo "$line"
done < "$filename"

