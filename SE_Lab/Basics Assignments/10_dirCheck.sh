#!/bin/bash

dirname=$1

if [ -d "$dirname" ]; then
    echo "Directory '$dirname' already exists."
else
    mkdir "$dirname"
    echo "Directory '$dirname' created."
fi

echo "Operation completed."

