# Create a Student class with a method to calculate average marks. 
class Student:
    def __init__(self,maths,eng,che,phy):
        self.maths=maths
        self.eng=eng
        self.che=che
        self.phy=phy
        self.Total_marks=sum([self.maths,self.eng,self.che,self.phy])
    def Avg_marks(self):
        Avgmarks = self.Total_marks/4
        print("Avgmarks:",Avgmarks)
student=Student(50,60,70,80) 
student.Avg_marks()