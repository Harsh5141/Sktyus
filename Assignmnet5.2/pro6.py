# Write a program to read a file and print only lines containing a specific word.
filename = r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt"
word_to_search = input("Enter the word to search for: ").lower() 
try:
    with open(filename, "r") as file:
        for line in file:
            if word_to_search in line.lower():  
                print(line, end="") 
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")