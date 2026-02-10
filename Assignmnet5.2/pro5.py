# Write a program to append a list of strings to an existing file.
filename = r"C:\Users\meet1\OneDrive\Desktop\Python\sentences.txt"
lines_to_append = ["My name is meet"]
with open(filename, "a") as file:
    for line in lines_to_append:
        file.write(line + "\n") 
print(f"Lines have been appended to '{filename}' successfully.")    