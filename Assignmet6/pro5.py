# Create an Employee class that displays salary details. 
class Employee:
    def __init__(self,day_basic_salary):
        self.day_basic_salary=day_basic_salary
    def salary1(self):
        month_day=int(input("enter a day in wok togo: "))
        bouns=5000
        if month_day >= 24:
            Total_salary=(month_day*self.day_basic_salary)+bouns
            print("salary:",Total_salary)
        elif month_day <= 24 and month_day>0 :
            Total_salary=(24-month_day*self.day_basic_salary)+bouns
            print("salary:",Total_salary)
        else:
            month_day=0
            Total_salary=0
            print("salary:",Total_salary)
emp =Employee(600)
emp.salary1()