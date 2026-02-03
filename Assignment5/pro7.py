# Write a program to handle IndexError when accessing a list.
num=[10,20,30,40,50]
try:
    index=int(input("Enter a  index: "))
    print("value at index:",num[index])
except IndexError:
    print("Error:index out of range")
except ValueError:
    print("Erroe:please enter a valid integer")