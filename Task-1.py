def factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(1, number + 1):
        result *= value

    return result


number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number} is: {factorial(number)}")
