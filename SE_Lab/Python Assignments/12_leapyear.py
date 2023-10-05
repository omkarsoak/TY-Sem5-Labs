try:
    start_year = int(input("Enter a year: "))
    if start_year < 0:
        raise ValueError("Year cannot be negative.")

    leap_years_found = 0

    while leap_years_found < 10:
        if (start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0):
            print(start_year)
            leap_years_found += 1
        start_year += 1

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
