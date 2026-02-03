# Write a program to handle division by zero error.
num1=int(input("Enter a num: "))
num2=int(input("Enter a num: "))
try:
    result=num1/num2
    print("Result: ",result)
except ZeroDivisionError:
    print("Error division by zero is not allowed")