#!/bin/bash

#command line argument
file1=$1
file2=$2

if cmp -s "$file1" "$file2"; then
    echo "The contents of '$file1' and '$file2' are the same."
else
    echo "The contents of '$file1' and '$file2' are different."
fi

