# Create a class with private attributes and getter/setter methods.
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age >0:
            self.__age=age
        else:
            print("Age must be positive")
s = Student("Meet", 21)
print(s.get_name())
print(s.get_age())
s.set_name("Alay")
s.set_age(25)
print(s.get_name())
print(s.get_age())
  
