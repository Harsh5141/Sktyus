# 9 Write a program to read a CSV file and display its content in a formatted way.

import csv
try:
    with open(r"c:\Users\meet1\OneDrive\Desktop\Python\m.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)

        print(f"{' | '.join(headers)}")
        print("-" * 40)

        for row in csvreader:
            print(f"{' | '.join(row)}")
except FileNotFoundError:
    print("Error: CSV file not found!!.")