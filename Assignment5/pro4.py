# Write a program to demonstrate multiple exception blocks.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Calculation successful.")