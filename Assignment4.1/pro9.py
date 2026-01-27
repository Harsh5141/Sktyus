#Simple calculator (add, subtract, multiply, divide).
num1=int(input("Enter a num: "))
num2=int(input("Enter a num: "))
operation=input("enter a operation:(+,-,*,/,%): ")
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
elif operation == "%":
    print(num1%num2)
else:
    print("Invalid operation.")