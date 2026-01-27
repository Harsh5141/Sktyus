#2 Grade calculator based on marks: 90+ = A, 80+ = B, else C.
Marks=int(input("enter a marks: "))
if Marks >=95<=100:
    print("Grade A+")
if Marks >=90<=95:
    print("Grade A")
if Marks >=80<=90:
    print("Grade B")
if Marks >=70<=80:
    print("Grade c")
if Marks >=60 <=70:
    print("Grade D")
if Marks >=50 <=60:
    print("Grade E")
else:
    print("Fail")
