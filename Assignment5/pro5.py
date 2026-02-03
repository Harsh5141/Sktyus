# Write a program to use finally for resource cleanup.
try:
    file = open("Ass2.py","r")
    print(file.read())
except FileNotFoundError:
    print("Error:file not found")
finally:
    print("File close successfully") 