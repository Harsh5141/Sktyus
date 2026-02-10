# 10 Write a program to back up a file by copying its contents into another file.
try:
    with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "r") as source_file:
        content = source_file.read()

    with open(r"c:\Users\meet1\OneDrive\Desktop\Python\sample2.txt", "a") as backup_file:
        backup_file.write(content)

    print("File backup created successfully.")

except FileNotFoundError:
    print("Error: Original file not found.")