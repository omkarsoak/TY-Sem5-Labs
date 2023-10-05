#!/bin/bash

read -p "Enter the cost price: " cost_price
read -p "Enter the selling price: " selling_price

if (( cost_price < 0 || selling_price < 0 )); then
    echo "Error: Cost price and selling price must be non-negative numbers."
    exit 1
fi

if (( cost_price > selling_price )); then
    echo "Loss: $((cost_price - selling_price))"
elif (( cost_price <= selling_price )); then
    echo "Profit: $((selling_price - cost_price))"

fi


