# 8 Write a program to merge the contents of two text files into a third file.
file1=input("Enter the first file name:")
file2=input("Enter the second file name:")
file3=input("Enter the output file name:")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()
    with open(file3, "w") as f3:
        f3.write(content1 + "\n" + content2)
    print("Files merged successfully into", file3)
except FileNotFoundError:
    print("Error: One or more files not found.")