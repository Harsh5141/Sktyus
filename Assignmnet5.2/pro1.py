# Write a program to read a file and display its contents.
with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "r") as file:
    content = file.read()
    print(content)