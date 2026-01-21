#Write a program that uses and & or operators to check multiple conditions.

a = int (input("enter the frist number:"))
b = int (input("enter the second number:"))

if a>0 and b>0:
    print("bothe numbars are positve:")

    if a>0 or b>0:
        print ("last number is positve:")
    else:
        print("no numbar is positve")