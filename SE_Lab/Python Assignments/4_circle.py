import math

try:
    radius = float(input("Enter the radius of the circle in cm: "))

    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    area = math.pi * radius**2

    circumference = 2 * math.pi * radius

    print(f"The area of the circle is: {area:.2f} square cm")
    print(f"The circumference of the circle is: {circumference:.2f} cm")

except ValueError as e:
    print(f"Error: {e}")
