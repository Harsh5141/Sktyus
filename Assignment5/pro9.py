# Write a program to log errors to a file instead of printing them.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except Exception as e:
    file = open("Ass4.py","a")
    file.write(str(e)+"\n")
    file.close()