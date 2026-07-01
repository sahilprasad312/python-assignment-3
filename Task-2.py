import math


number = float(input("Enter a number: "))

if number <= 0:
    print("Please enter a positive number for square root and logarithm calculations.")
else:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    print(f"Square root: {square_root}")
    print(f"Logarithm: {natural_log}")
    print(f"Sine: {sine_value}")
