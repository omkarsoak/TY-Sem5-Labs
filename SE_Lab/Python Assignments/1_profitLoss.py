try:
    # Input cost price and selling price as floating-point numbers
    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))

    # Check if cost price and selling price are non-negative
    if cost_price < 0 or selling_price < 0:
        print("Cost price and selling price must be non-negative.")
    else:
        # Check if cost price is less than selling price
        if cost_price < selling_price:
            profit = selling_price - cost_price
            print(f"Profit: ${profit:.2f}")
        elif cost_price > selling_price:
            loss = cost_price - selling_price
            print(f"Loss: ${loss:.2f}")
        else:
            print("No profit, no loss.")

except ValueError:
    print("Invalid input. Please enter valid numerical values for cost price and selling price.")
