# Write a program to create a custom exception for invalid age (<18).
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age<18:
        raise InvalidAgeError("Age must be 18 or above")
    print("acess granted")
except InvalidAgeError as e:
    print("custom exception:",e)
except ValueError:
    print("Please enter a valid number")