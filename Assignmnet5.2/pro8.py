# 7 Write a program to replace a specific word in a file and save changes.
specific_word = input("Enter the word to be replaced: ")
replacement_word = input("Enter the replacement word: ")
try:
    with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "r") as file:
        content = file.read()

    updated_content = content.replace(specific_word, replacement_word)

    with open(r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt", "a") as file:
        file.write(updated_content)
    print("Word replaced successfully.")
except FileNotFoundError:
    print("Error: File not found.")