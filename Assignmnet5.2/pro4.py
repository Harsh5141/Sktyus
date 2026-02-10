# Write a program to write 5 user-entered sentences to a file.
filename = r"C:\Users\meet1\OneDrive\Desktop\Python\sentences.txt"
with open(filename, "w") as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        file.write(sentence + "\n")  
print(f"5 sentences have been written to '{filename}' successfully.")