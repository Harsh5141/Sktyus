# Create a Teacher and Student class to show inheritance.
class Teacher:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub
    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.sub}")
class Student(Teacher):  
    def __init__(self, name, sub, enrollment_no):
        super().__init__(name, sub)  
        self.enrollment_no = enrollment_no
    def Num(self):
        print(f"Enrollment No: {self.enrollment_no}")
s = Student("Meet", "Maths", 101)
s.display()  
s.Num()     
