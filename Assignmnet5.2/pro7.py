# 6 Write a program to read a file and print only lines containing a specific word.

specific_word = input("Enter the word to search for: ")
try:
    with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "r") as file:
        lines = file.readlines()
        print(f"Lines containing the word '{specific_word}':")
        for line in lines:
            if specific_word in line:
                print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")