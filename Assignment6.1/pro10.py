# Demonstrate the use of super() in inheritance.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"Name:{self.name},Age:{self.age}")
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    def show(self):
        super().show()
        print(f"Employee_Id:{self.employee_id}")
E=Employee("Meet",29,33)
E.show()