# Write a program to count how many times each word appears in a file.
filename = r"C:\Users\meet1\OneDrive\Desktop\Python\sample.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
    words = content.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.items():
        print(f"{word}: {count}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
