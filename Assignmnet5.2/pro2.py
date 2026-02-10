# Write a program to count the number of lines in a file.
filename=r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt"
try:
    with open(filename,"r") as file:
        line_count =sum(1 for line in file)
    print(f"numbers of lines in'{filename}':{line_count}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")