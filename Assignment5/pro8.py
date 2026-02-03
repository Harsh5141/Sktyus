# Write a program that takes two numbers and handles all possible errors.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Program execution completed.")